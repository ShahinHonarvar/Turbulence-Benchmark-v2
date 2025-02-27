from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(1, len(num_str)):
            if not isprime(int(num_str[i:])) or not isprime(int(num_str[:i])):
                return False
        return True
    x = numbers[23]
    primes = [num for num in range(2, x + 1) if isprime(num) and is_truncatable_prime(num)]
    return primes