def all_left_right_truncatable_prime(args):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = args[55]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    str_primes = [str(p) for p in primes]

    def remove_digit(s):
        return [int(s[:i] + s[i + 1:]) for i in range(len(s))]
    truncatable_primes = [p for p in primes if all((is_prime(int(str(p)[i:j])) for i in range(len(str(p))) for j in range(i + 1, len(str(p)) + 1) if len(str(p))[i:j] != '0'))]
    return truncatable_primes