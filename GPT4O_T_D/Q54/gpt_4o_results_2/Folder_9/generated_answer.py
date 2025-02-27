from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        str_n = str(n)
        while str_n:
            if not isprime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    if len(numbers) <= 29:
        return []
    x = numbers[29]
    result = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(result, reverse=True)