def if_decimal_is_divisible(binary_rep):
    num = int(binary_rep, 2)
    a, b = (0, 1)
    fib_nums = [0, 1]
    for i in range(2, 180):
        a, b = (b, a + b)
        fib_nums.append(b)
    if num % fib_nums[179] == 0:
        return True
    else:
        return False