from sympy import isprime

def all_left_right_truncatable_prime(tup):

    def is_left_right_truncatable(n):
        while n > 9:
            if not isprime(n) or n % 10 == 0:
                return False
            n = int(str(n)[1:-1])
        return True
    if len(tup) < 370:
        return 'Input tuple should have at least 370 elements.'
    x = tup[369]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)