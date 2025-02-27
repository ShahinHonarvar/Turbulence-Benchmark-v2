from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        while len(num_str) > 1:
            if not (isprime(int(num_str)) and isprime(int(num_str[1:])) and isprime(int(num_str[:-1]))):
                return False
            num_str = num_str[1:-1]
        return isprime(int(num_str))
    x = numbers[70]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes