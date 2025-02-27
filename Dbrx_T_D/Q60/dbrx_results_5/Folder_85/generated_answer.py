from sympy import isprime

def all_left_right_truncatable_prime(args):

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[:-1])
        return True
    x = args[94]
    result = []
    for num in range(2, x + 1):
        if isprime(num) and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)