def all_left_truncatable_prime(x, y):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_tables = [1]
    for i in range(2, x):
        if is_prime(i):
            prime_tables.append(i)
    left_truncatable_primes = []
    for num in prime_tables:
        if str(num)[::-1].replace('0', '', 1)[::-1] == str(num) and len(str(num)) > 1:
            left_truncatable_primes.append(num)
    left_truncatable_primes = list(set(left_truncatable_primes))
    left_truncatable_primes.sort()
    return left_truncatable_primes[:y]