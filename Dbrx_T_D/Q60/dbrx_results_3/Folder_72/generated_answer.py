from sympy import isprime

def all_left_right_truncatable_prime(tup):

    def is_left_right_truncatable_prime(n):
        if not (str(n).count('0') == 0 and isprime(n)):
            return False
        s = str(n)
        for i in range(1, len(s)):
            if not (isprime(int(s[i:])) and isprime(int(s[:-i]))):
                return False
        return True
    x = tup[31]
    return sorted([i for i in range(10, x + 1) if is_left_right_truncatable_prime(i)], reverse=True)