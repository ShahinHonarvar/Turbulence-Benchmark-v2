def all_left_right_truncatable_prime(x):

    def is_truncatable_prime(n):
        if str(n).count('0') > 0:
            return False
        while len(str(n)) > 1:
            if not is_prime(n):
                return False
            n = n % 10 ** (len(str(n)) - 2)
            if not is_prime(n):
                return False
        return is_prime(n)

    def is_prime(n):
        if n < 2:
            return False
        elif n == 2 or n == 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        sqrt_n = int(n ** 0.5) + 1
        while i <= sqrt_n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    primes.sort(reverse=True)
    return [i for i in primes if is_truncatable_prime(i)]