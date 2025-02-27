def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    if len(numbers) < 30:
        return []
    x = numbers[29]
    left_truncatable_primes = []

    def is_left_truncatable_prime(p):
        str_p = str(p)
        while str_p:
            if '0' in str_p or not is_prime(int(str_p)):
                return False
            str_p = str_p[1:]
        return True
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)