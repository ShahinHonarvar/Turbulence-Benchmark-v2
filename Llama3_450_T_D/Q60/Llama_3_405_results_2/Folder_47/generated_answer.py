def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[49]
    truncatable_primes = set()
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        str_num = str(num)
        is_truncatable_prime = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                is_truncatable_prime = False
                break
            if not is_prime(int(str_num[:-i or None])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime and is_prime(num):
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes))