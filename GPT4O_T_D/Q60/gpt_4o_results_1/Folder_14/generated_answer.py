from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable(num):
        s = str(num)
        for i in range(1, len(s)):
            if not (isprime(int(s[i:])) and isprime(int(s[:-i]))):
                return False
        return True
    if len(numbers) <= 78:
        return []
    x = numbers[78]
    result = []
    for num in range(10, x + 1):
        if '0' not in str(num) and isprime(num) and is_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)