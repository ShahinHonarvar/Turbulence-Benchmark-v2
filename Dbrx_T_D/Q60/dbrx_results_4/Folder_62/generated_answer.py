from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):

    def is_left_right_truncatable_prime(n):
        if not isprime(n) or '0' in str(n):
            return False
        while n > 9:
            n = n % 10 ** n.bit_length() // 10
            if not isprime(n):
                return False
        return True
    upper_bound = numbers_tuple[70]
    return [i for i in range(10, upper_bound + 1) if is_left_right_truncatable_prime(i)]