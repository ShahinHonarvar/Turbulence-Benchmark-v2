def all_left_right_truncatable_prime(lst):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = lst[46]
    truncatable_primes = []
    for num in range(x, 1, -1):
        if is_prime(num):
            n = num
            while n != 0 and n != 2:
                n = int(n / 10)
            if n == 2:
                truncatable_primes.append(num)
    for prime in truncatable_primes:
        if not all_left_right_truncatable_prime([prime]):
            truncatable_primes.remove(prime)
    return sorted(truncatable_primes, reverse=True)