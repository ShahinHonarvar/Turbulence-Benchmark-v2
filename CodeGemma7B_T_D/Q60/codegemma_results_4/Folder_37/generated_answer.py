from sympy import sqrt, isprime  # Import sqrt and isprime functions

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[35]

    def is_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(1, len(num_str)):
            if not isprime(int(num_str[i:])):
                return False
        for i in range(len(num_str) - 1):
            if not isprime(int(num_str[:-i - 1])):
                return False
        return True
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)