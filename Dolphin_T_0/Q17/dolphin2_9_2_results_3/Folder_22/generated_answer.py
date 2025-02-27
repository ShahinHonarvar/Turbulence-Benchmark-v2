def all_ints_div_by_both_two_nums(numbers):
    filtered_numbers = [n for n in numbers[40:201] if n % 21 == 0 and n % 71 == 0]
    return filtered_numbers