def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(prime):
        if '0' in str(prime):
            return False
        str_prime = str(prime)
        for i in range(len(str_prime)):
            if not is_prime(int(str_prime[i:])):
                return False
        return True
    if len(numbers) <= 67:
        return []
    x = numbers[67]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)