def find_second_largest_num(list_of_numbers):
    if len(list_of_numbers) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in list_of_numbers:
        if num > max_num:
            max_num, second_max_num = (num, max_num)
        elif max_num > num > second_max_num:
            second_max_num = num
    return second_max_num