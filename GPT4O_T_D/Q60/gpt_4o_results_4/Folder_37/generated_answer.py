from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def truncatable(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not s or not isprime(int(s)):
                return False
        return True
    x = numbers[35]
    return sorted([n for n in range(10, x + 1) if isprime(n) and truncatable(n) and ('0' not in str(n))], reverse=True)