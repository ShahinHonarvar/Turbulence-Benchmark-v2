from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        while s:
            if not isprime(int(s)):
                return False
            s = s[1:]
        return True
    x = numbers[36]
    result = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(result, reverse=True)