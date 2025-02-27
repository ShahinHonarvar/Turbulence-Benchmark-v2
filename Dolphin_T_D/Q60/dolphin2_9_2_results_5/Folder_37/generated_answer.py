def all_left_right_truncatable_prime(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        return all((is_prime(int(str(n)[i:j])) for i in range(len(str(n))) for j in range(len(str(n)) + 1 - i)))

    def get_truncatable_primes(n):
        i = 2
        primes = []
        while i <= n:
            if is_truncatable(i):
                primes.append(i)
            i += 1
        return primes[::-1]
    x = lst[35]
    return get_truncatable_primes(x)