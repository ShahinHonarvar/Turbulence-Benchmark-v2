def all_ints_not_div_by_num(numbers, index1, index2):
    return [num for num in numbers[index1:index2] if num % 8 != 0]