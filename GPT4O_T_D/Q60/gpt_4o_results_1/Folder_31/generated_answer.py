from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_lr_truncatable_prime(num):
        if '0' in str(num):
            return False
        s = str(num)
        while len(s) > 1:
            if not (isprime(int(s)) and isprime(int(s[:-1])) and isprime(int(s[1:]))):
                return False
            s = s[1:-1]
        return isprime(int(s))
    x = numbers[50]
    result = [n for n in range(2, x + 1) if isprime(n) and is_lr_truncatable_prime(n)]
    result.sort(reverse=True)
    return result