def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    left_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((is_prime(int(str_num[i:])) for i in range(len(str_num)))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)