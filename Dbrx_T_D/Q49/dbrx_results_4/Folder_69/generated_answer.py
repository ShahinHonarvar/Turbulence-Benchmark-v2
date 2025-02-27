def if_decimal_is_divisible(binary_rep):
    decimal_num = int(binary_rep, 2)
    fibonacci_nums = [0, 1]
    while True:
        next_fib = fibonacci_nums[-1] + fibonacci_nums[-2]
        if next_fib > 170:
            break
        fibonacci_nums.append(next_fib)
    return decimal_num % fibonacci_nums[170] == 0