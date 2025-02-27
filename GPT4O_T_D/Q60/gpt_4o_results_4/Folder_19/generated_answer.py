from sympy import isprime

def all_left_right_truncatable_prime(input_tuple):

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(1, len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:-i])):
                return False
        return True
    x = input_tuple[67]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and isprime(num) and is_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)