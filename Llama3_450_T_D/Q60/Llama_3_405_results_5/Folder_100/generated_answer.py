def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[26]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num):
            str_num = str(num)
            truncatable = True
            for i in range(len(str_num)):
                if not (is_prime(int(str_num[i + 1:])) and (is_prime(int(str_num[:-1 - i])) or len(str_num) - 1 - i < 2)):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(num)
    return truncatable_primes