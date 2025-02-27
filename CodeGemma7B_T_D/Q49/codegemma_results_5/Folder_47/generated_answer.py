from sys import stdin

def decimal_to_int(binary):
    n = len(binary)
    result = 0
    b = 1
    for i in range(n):
        digit = binary[n - i - 1]
        if digit == '1':
            result += b
        b *= 2
    return result

def fibonacci(limit):
    nums = [0, 1]
    while nums[-1] < limit:
        nums.append(nums[-1] + nums[-2])
    return nums

def if_decimal_is_divisible(binary):
    int_num = decimal_to_int(binary)
    fib_num = fibonacci(94)[-1]
    if int_num % fib_num == 0:
        return True
    else:
        return False