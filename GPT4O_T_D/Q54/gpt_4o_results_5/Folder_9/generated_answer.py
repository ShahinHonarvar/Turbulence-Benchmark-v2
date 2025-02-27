from sympy import isprime

def all_right_truncatable_prime(integers):

    def is_right_truncatable(number):
        number_str = str(number)
        while number_str:
            if not isprime(int(number_str)):
                return False
            number_str = number_str[:-1]
        return True
    x = integers[29]
    right_truncatable_primes = [n for n in range(2, x) if is_right_truncatable(n)]
    return sorted(right_truncatable_primes, reverse=True)