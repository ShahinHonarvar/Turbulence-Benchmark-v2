def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[175]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        str_num = str(num)
        is_left_right_truncatable_prime = True
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                is_left_right_truncatable_prime = False
                break
        if is_left_right_truncatable_prime and is_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)