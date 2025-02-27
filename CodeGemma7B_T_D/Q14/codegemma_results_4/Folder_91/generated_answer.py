def find_second_smallest_num(num_list):
    if len(num_list) <= 5:
        return 'None'
    min_num, second_min_num = (min(num_list), min(num_list))
    for num in num_list:
        if num < min_num:
            second_min_num, min_num = (min_num, num)
        elif num < second_min_num:
            second_min_num = num
    return second_min_num if second_min_num >= min_num else 'None'