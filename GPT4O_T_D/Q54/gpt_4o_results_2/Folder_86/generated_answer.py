from sympy import isprime

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 126:
        return []
    x = numbers[126]
    right_truncatable_primes = []

    def is_right_truncatable_prime(num):
        str_num = str(num)
        while str_num:
            if not isprime(int(str_num)):
                return False
            str_num = str_num[:-1]
        return True
    for number in range(2, x):
        if is_right_truncatable_prime(number):
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes, reverse=True)