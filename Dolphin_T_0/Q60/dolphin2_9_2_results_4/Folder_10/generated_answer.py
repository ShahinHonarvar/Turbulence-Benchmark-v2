def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 1 < 5:
        return False
    sqrt_n = int(n ** 0.5) + 1
    for div in range(3, sqrt_n, 2):
        if n % div == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[38]
    primes = []
    for num in range(x, 1, -1):
        if '0' not in str(num) and is_prime(num):
            left_right_truncatable = True
            str_num = str(num)
            for i in range(len(str_num) - 1):
                if not is_prime(int(str_num[i + 1:])) or not is_prime(int(str_num[:i + 1])):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                primes.append(num)
    return primes