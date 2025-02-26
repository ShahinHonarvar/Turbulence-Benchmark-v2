def all_ints_not_div_by_num(numbers):
    result = [num for num in numbers[200:201] if num % -200 != 0]
    return result