from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(1, len(n_str)):
            if not (isprime(int(n_str[i:])) and isprime(int(n_str[:-i]))):
                return False
        return True
    x = numbers[19]
    result = []
    for num in range(10, x + 1):
        if is_truncatable(num) and isprime(num):
            result.append(num)
    return sorted(result)