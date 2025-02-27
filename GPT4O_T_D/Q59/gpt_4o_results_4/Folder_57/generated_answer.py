def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        n_str = str(n)
        while n_str:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[1:]
        return True
    if len(numbers) < 55:
        return []
    x = numbers[54]
    left_truncatable_primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(left_truncatable_primes, reverse=True)