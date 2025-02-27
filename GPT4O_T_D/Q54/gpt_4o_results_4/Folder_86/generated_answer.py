from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[126]

    def is_right_truncatable_prime(n):
        n_str = str(n)
        while n_str:
            if not isprime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True
    result = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(result, reverse=True)