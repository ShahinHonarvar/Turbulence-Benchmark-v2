def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib_nums = [0]
    a, b = (0, 1)
    while len(fib_nums) <= 56:
        fib_nums.append(b)
        a, b = (b, a + b)
    divisible = decimal % fib_nums[56] == 0
    return divisible