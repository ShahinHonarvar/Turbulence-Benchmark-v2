def find_second_largest_num(my_list):
    if len(my_list) < 4:
        return None
    first = second = float('-inf')
    for i in my_list[0:4]:
        if i > first:
            first, second = (i, first)
        elif i > second and i != first:
            second = i
    return second if second != float('-inf') else None