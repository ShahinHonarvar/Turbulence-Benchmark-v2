from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[19]

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        while len(str_n) > 1:
            if not isprime(int(str_n)):
                return False
            str_n = str_n[1:-1]
        return isprime(int(str_n))
    result = []
    for num in range(10, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result)