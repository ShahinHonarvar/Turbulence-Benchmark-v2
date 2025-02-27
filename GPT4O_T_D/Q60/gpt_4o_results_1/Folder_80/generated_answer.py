from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            if not isprime(int(s)):
                return False
            s = s[1:-1]
        return isprime(n)
    x = numbers[14]
    result = [i for i in range(2, x + 1) if '0' not in str(i) and is_truncatable_prime(i)]
    return sorted(result, reverse=True)