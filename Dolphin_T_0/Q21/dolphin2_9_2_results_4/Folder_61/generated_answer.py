def all_ints_div_by_num(numbers):
    divisible_numbers = [n for n in numbers if n % 7 == 0]
    if 0 <= divisible_numbers[0] <= len(divisible_numbers):
        return divisible_numbers[0:1]
    else:
        return []