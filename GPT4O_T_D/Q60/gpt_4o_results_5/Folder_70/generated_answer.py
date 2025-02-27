from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str or not isprime(num):
            return False
        length = len(num_str)
        for i in range(1, length):
            left_truncated = int(num_str[i:])
            right_truncated = int(num_str[:-i])
            if not (isprime(left_truncated) and isprime(right_truncated)):
                return False
        return True
    x = numbers[433]
    results = []
    for i in range(10, x + 1):
        if is_truncatable_prime(i):
            results.append(i)
    return sorted(results, reverse=True)