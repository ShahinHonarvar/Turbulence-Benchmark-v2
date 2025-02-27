def find_second_largest_num(num_list):
    if len(num_list) < 5:
        return None
    maximum = max(num_list[0:5])
    second_maximum = float('-inf')
    for i in num_list[0:5]:
        if i < maximum and i > second_maximum:
            second_maximum = i
    if second_maximum != float('-inf'):
        return second_maximum
    else:
        return None