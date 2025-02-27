def find_second_smallest_num(numbers):
    sub_list = numbers[661:925]
    if len(set(sub_list)) < 2:
        return None
    else:
        return sorted(set(sub_list))[1]