def if_decimal_is_divisible(binary_str):
    fib_nums = [0, 1]
    for _ in range(2, 109):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    fibonacci_108th = fib_nums[108]
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_108th == 0