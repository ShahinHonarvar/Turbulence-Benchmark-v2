def if_decimal_is_divisible(bin_repr_decimal: str) -> bool:
    decimal_int = int(bin_repr_decimal, 2)
    fibonacci_nums = [0, 1]
    while len(fibonacci_nums) < 159:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    return decimal_int % fibonacci_nums[-1] == 0