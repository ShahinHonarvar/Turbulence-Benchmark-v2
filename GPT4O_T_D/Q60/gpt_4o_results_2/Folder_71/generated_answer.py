from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s) - 1):
            if not isprime(int(s[i + 1:])) or not isprime(int(s[:-(i + 1)])):
                return False
        return isprime(n)
    x = numbers[22]
    results = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(results, reverse=True)