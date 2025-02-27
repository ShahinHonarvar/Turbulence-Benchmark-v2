def all_ints_div_by_both_two_nums(numbers):
    start_index = 28
    end_index = 96
    result = [n for n in numbers[start_index:end_index + 1] if n % 90 == 0 and n % 97 == 0]
    return result