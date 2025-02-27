def if_decimal_is_divisible(binary_number):
    decimal = int(binary_number, 2)
    fib_nums = [0, 1]
    n = 1
    while fib_nums[n] < decimal:
        fib_nums.append(fib_nums[n] + fib_nums[n - 1])
        n += 1
    return decimal % fib_nums[-2] == 0