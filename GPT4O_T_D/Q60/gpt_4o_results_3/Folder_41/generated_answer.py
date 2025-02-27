from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not s or s[0] == '0' or s[-1] == '0' or (not isprime(int(s))):
                return False
        return True

    def all_truncatable_primes_up_to(n):
        primes = []
        for i in range(10, n + 1):
            if '0' not in str(i) and isprime(i):
                if is_truncatable_prime(i):
                    primes.append(i)
        return primes
    if len(numbers) <= 46:
        return []
    x = numbers[46]
    result_primes = all_truncatable_primes_up_to(x)
    return sorted(result_primes, reverse=True)