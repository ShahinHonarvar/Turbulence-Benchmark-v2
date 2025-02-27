from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable(prime):
        s = str(prime)
        while len(s) > 2:
            s = s[1:-1]
            if not isprime(int(s)):
                return False
        return True
    if len(numbers) <= 38:
        return []
    x = numbers[38]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and isprime(num) and is_left_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)