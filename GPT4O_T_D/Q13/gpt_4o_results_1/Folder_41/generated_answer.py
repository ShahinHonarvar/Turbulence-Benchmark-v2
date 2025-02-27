def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    sub_list = numbers[6:7]
    if len(sub_list) < 2:
        return None
    first_max = second_max = float('-inf')
    for num in sub_list:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max:
            second_max = num
    return second_max if second_max != float('-inf') else None