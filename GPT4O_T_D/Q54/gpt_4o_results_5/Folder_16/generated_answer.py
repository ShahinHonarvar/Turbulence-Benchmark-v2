from sympy import isprime

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 792:
        return []
    x = numbers[792]

    def is_right_truncatable_prime(num):
        num_str = str(num)
        while num_str:
            if not isprime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return True
    result = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    return sorted(result)