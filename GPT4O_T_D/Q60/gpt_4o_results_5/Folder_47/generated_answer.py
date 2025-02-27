import sympy

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable(prime):
        s = str(prime)
        for i in range(len(s)):
            if not sympy.isprime(int(s[i:])) or not sympy.isprime(int(s[:len(s) - i])):
                return False
        return True
    x = numbers[49]
    result = []
    for num in range(10, x + 1):
        if sympy.isprime(num) and is_left_right_truncatable(num):
            result.append(num)
    return result