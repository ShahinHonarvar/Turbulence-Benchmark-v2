def all_ints_div_by_num(numbers):
    start_index = 574
    end_index = 744
    result = [num for num in numbers[start_index:end_index + 1] if num % 649 == 0]
    return result