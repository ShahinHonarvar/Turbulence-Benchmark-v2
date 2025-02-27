from sympy import isprime

def all_left_right_truncatable_prime(n):

    def is_left_right_truncatable_prime(num):
        if '0' in str(num) or len(str(num)) < 2:
            return False
        for i in range(len(str(num)) - 1):
            if not isprime(int(str(num)[:i + 1])) or not isprime(int(str(num)[i + 1:])):
                return False
        return True
    return sorted(set(filter(is_left_right_truncatable_prime, range(11, n + 1))))[::-1]