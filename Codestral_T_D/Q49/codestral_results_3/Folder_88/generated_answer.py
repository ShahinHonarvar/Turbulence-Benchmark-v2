def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_nums = [0, 1]
    while len(fib_nums) < 49:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    fib_49 = fib_nums[-1]
    return decimal % fib_49 == 0