def all_ints_div_by_both_two_nums(numbers):
    range_start, range_end = (306, 957)
    result = [num for num in numbers[range_start:range_end + 1] if num % 982 == 0 and num % 319 == 0]
    return result