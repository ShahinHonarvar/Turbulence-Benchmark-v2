def if_decimal_is_divisible(bin_str):
    fibonacci_nums = [0, 1]
    num = int(bin_str, 2)
    while fibonacci_nums[-1] < num:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    seventh_seven_fibonacci = fibonacci_nums[76]
    return num % seventh_seven_fibonacci == 0