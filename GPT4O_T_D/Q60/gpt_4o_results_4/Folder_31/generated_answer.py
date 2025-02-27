from sympy import isprime

def all_left_right_truncatable_prime(args):

    def is_truncatable(prime):
        str_num = str(prime)
        if '0' in str_num:
            return False
        n = len(str_num)
        for i in range(1, n):
            if not (isprime(int(str_num[i:])) and isprime(int(str_num[:n - i]))):
                return False
        return True
    x = args[50]
    primes = []
    for num in range(11, x + 1):
        if isprime(num) and is_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)