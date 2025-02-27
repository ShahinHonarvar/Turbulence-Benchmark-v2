from sympy import isprime

def all_left_right_truncatable_prime(t):

    def is_left_right_truncatable_prime(n):
        s = str(n)
        return '0' not in s and all((isprime(int(s[i:len(s) - i])) for i in range(len(s))))
    x = t[42]
    return sorted(filter(is_left_right_truncatable_prime, range(x + 1)))