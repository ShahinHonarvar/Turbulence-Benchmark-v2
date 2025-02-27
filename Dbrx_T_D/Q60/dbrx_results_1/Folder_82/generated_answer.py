from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):

    def is_left_right_prime(n):
        s = str(n)
        if '0' in s or len(s) == 1:
            return False
        while len(s) > 1:
            if not isprime(int(s)):
                return False
            s = s[1:] if s[0] == '1' else s[:-1]
        return True
    return sorted([x for x in range(2, min(numbers_tuple[69], 10000)) if is_left_right_prime(x)], reverse=True)