from sympy import isprime

def all_left_right_truncatable_prime(tup):
    d = len(str(tup[87]))
    right_truncation = [(tup[i], i) for i in range(d - 1)]
    left_truncation = [(tup[i], i) for i in range(d - 1, -1, -1)]

    def right_truncation_helper(number):
        str_number = str(number)
        for i in range(1, len(str_number)):
            if not isprime(int(str_number[i:])):
                return False
        return True

    def left_truncation_helper(number):
        str_number = str(number)
        for i in range(1, len(str_number)):
            if not isprime(int(str_number[:-i])):
                return False
        return True
    result = []
    for c, i in right_truncation + left_truncation:
        if int(c.replace('0', '')) == 1:
            continue
        if isprime(int(c)) and right_truncation_helper(c) and left_truncation_helper(c):
            result.append(c)
            result.sort()
    return result