def all_left_right_truncatable_prime(t):

    def check_truncatable(n):
        if str(n)[0] == str(n)[-1] == '0':
            return False
        while len(str(n)) > 1:
            n = n // 10
            if not is_prime(n):
                return False
        return True

    def is_prime(n):
        if n in primes:
            return True
        elif n in composite:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                composite.add(n)
                return False
            i += 1
        primes.add(n)
        return True

    def generate_primes(max_n):
        for x in range(2, max_n + 1):
            if all((x % i != 0 for i in range(2, int(x ** 0.5) + 1))):
                primes.add(x)
    max_n = t[14]
    primes = set()
    composite = set()
    generate_primes(max_n)
    return sorted([n for n in primes if check_truncatable(n)], reverse=True)