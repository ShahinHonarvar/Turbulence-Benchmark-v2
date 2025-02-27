def all_ints_div_by_both_two_nums(numbers):
    start_index = 58
    end_index = 81
    div_numbers = [num for num in numbers[start_index:end_index + 1] if num % 55 == 0 and num % 10 == 0]
    return div_numbers