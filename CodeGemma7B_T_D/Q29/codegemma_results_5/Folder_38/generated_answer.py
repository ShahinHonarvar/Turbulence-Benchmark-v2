def gcf_two_nums(numbers):
    first_num = numbers[88]
    second_num = numbers[35]
    while first_num != second_num:
        if first_num > second_num:
            first_num = first_num - second_num
        else:
            second_num = second_num - first_num
    return first_num