from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable(prime):
        s = str(prime)
        while len(s) > 1:
            s = s[1:-1]
            if s and (not isprime(int(s))):
                return False
        return True
    x = numbers[52]
    result = []
    for num in range(2, x + 1):
        if isprime(num) and is_left_right_truncatable(num) and ('0' not in str(num)):
            result.append(num)
    return sorted(result, reverse=True)