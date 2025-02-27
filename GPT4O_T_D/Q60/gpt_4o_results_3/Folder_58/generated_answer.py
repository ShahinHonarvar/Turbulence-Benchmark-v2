from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 976:
        return []
    x = numbers[975]
    left_right_truncatable_primes = []

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n or not isprime(n):
            return False
        length = len(str_n)
        for i in range(1, length):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:-i])):
                return False
        return True
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)