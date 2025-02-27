from functools import reduce

def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def last_num_in_fibonacci(binary):
    num = reduce(lambda x, y: x * 2 + y, map(int, binary))
    return fibonacci(num) % 10

def if_decimal_is_divisible(binary):
    res = last_num_in_fibonacci(binary)
    if res == 0 or res == 1:
        if res == 0:
            return True
        else:
            return False
    else:
        return not (binary[-1] == '0' and if_decimal_is_divisible(binary[:-1]))