from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not s or not isprime(int(s)):
                return False
        return True
    x = numbers[11]
    truncatable_primes = []
    for num in range(10, x + 1):
        if isprime(num):
            str_num = str(num)
            if '0' not in str_num and is_truncatable_prime(num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)