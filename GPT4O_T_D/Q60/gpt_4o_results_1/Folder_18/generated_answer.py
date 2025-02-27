import sympy

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            if not sympy.isprime(int(str_n[i:])) or not sympy.isprime(int(str_n[:i])):
                return False
        return True
    x = numbers[429]
    result = []
    for num in range(2, x + 1):
        if sympy.isprime(num) and is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)