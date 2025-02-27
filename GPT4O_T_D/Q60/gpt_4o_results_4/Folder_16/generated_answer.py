import sympy

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        if '0' in str(n) or not sympy.isprime(n):
            return False
        s = str(n)
        while len(s) > 1:
            s = s[1:]
            if not sympy.isprime(int(s)):
                return False
        s = str(n)
        while len(s) > 1:
            s = s[:-1]
            if not sympy.isprime(int(s)):
                return False
        return True
    x = numbers[792]
    result = [num for num in range(10, x + 1) if is_truncatable_prime(num)]
    return result