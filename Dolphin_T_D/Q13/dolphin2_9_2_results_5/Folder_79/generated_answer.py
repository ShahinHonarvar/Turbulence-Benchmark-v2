def find_second_largest_num(my_list):
    if len(my_list) < 5:
        return None
    my_list = my_list[4:5]
    if len(my_list) < 2:
        return None
    max1, max2 = (my_list[0], -float('inf')) if my_list[0] > -float('inf') else (-float('inf'), my_list[0])
    for num in my_list[1:]:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    return max2 if max2 != -float('inf') else None