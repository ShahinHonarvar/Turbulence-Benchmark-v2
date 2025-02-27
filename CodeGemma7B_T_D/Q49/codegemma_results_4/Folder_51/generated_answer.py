def if_decimal_is_divisible(binary_str):
    length = len(binary_str)
    num = int(''.join(reversed(binary_str)), 2)
    i = 0
    num_fib = 0
    num_mul = 1
    while num_fib <= num:
        num_mul += 1
        num_fib = num_mul * (num_mul + 1)
        if num_fib == num:
            return True
        elif num_fib > num and num_fib <= 17 * length:
            continue
        elif num_fib > 17 * length and i == 15:
            return False
        i += 1