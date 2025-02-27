from sympy import isprime

def all_left_truncatable_prime(n):

    def is_left_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(1, len(n)):
            if not isprime(int(n[i:])):
                return False
        return True
    return sorted([num for num in range(1, n) if is_left_truncatable(num)], reverse=True)