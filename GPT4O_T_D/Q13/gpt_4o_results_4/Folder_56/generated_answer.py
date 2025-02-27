def find_second_largest_num(num_list):
    if len(num_list) <= 1:
        return None
    first_max = second_max = float('-inf')
    for num in num_list:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max:
            second_max = num
    return second_max if second_max != float('-inf') else None