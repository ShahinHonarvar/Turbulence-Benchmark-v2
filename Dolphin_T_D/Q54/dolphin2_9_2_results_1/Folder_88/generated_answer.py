def all_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = input_tuple[93]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            s = str(n)
            for i in range(1, len(s)):
                if not is_prime(int(s[i:])):
                    break
                if len(s) - i == 1:
                    primes.append(n)
    return sorted(primes)