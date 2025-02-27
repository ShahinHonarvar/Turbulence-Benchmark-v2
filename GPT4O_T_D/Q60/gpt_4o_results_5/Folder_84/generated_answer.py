from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable(p):
        str_p = str(p)
        if '0' in str_p:
            return False
        for i in range(1, len(str_p)):
            left_truncated = int(str_p[i:])
            right_truncated = int(str_p[:-i])
            if not (isprime(left_truncated) and isprime(right_truncated)):
                return False
        return True
    x = numbers[630]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if isprime(num) and is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)