from sympy import isprime

def all_right_truncatable_prime(numbers):
    if len(numbers) < 176:
        return []
    x = numbers[175]

    def is_right_truncatable_prime(n):
        str_n = str(n)
        while str_n:
            if not isprime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    result = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    return sorted(result)