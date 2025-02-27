import sympy

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            if not sympy.isprime(int(str_num[i:])) or not sympy.isprime(int(str_num[:-i])):
                return False
        return sympy.isprime(num)
    x = numbers[126]
    truncatable_primes = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)