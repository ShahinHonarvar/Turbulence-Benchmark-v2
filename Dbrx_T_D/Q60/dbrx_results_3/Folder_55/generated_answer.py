from sympy import isprime

def all_left_right_truncatable_prime(tup):

    def is_left_right_truncatable(n):
        for i in range(len(str(n))):
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        for i in range(len(str(n))):
            if not isprime(n):
                return False
            n = int(str(n)[:-1])
        return True
    x = tup[73]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)