def if_decimal_is_divisible(bin_str):
    decimal_num = int(bin_str, 2)
    fibonacci_num = 0
    current_num = 0
    next_num = 1
    for _ in range(185):
        fibonacci_num = current_num + next_num
        current_num = next_num
        next_num = fibonacci_num
    if decimal_num % fibonacci_num == 0:
        return True
    else:
        return False