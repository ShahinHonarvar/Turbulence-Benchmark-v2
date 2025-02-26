def all_ints_div_by_both_two_nums(numbers):
    result = [num for num in numbers[60:201] if num % 9 == 0 and num % 11 == 0]
    return result