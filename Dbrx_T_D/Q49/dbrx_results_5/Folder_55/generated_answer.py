def is_decimal_divisible(by_binary_str: str) -> bool:
    decimal_num = int(by_binary_str, 2)
    fibonacci_nums = [0, 1]
    while len(fibonacci_nums) < 39 or fibonacci_nums[-1] + fibonacci_nums[-2] < decimal_num:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    return decimal_num % fibonacci_nums[-2] == 0