from sympy import isprime

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 30:
        return []
    x = numbers[30]
    result = []

    def is_right_truncatable_prime(n):
        n_str = str(n)
        while n_str:
            if not isprime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True
    for n in range(2, x):
        if is_right_truncatable_prime(n):
            result.append(n)
    return sorted(result, reverse=True)