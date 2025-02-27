from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):

    def is_left_right_truncatable(n):
        if str(n)[0] == '0' or not isprime(n):
            return False
        while n > 9:
            n = int(str(n)[1:])
            if not isprime(n):
                return False
        return True
    x = numbers_tuple[29]
    result = []
    for num in range(1, x + 1):
        if is_left_right_truncatable(num):
            result.append(num)
    result.sort(reverse=True)
    return result