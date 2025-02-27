def find_second_smallest_num(numbers):
    if len(numbers) >= 12:
        sub_list = numbers[10:11]
        if len(set(sub_list)) >= 2:
            sorted_sub_list = sorted(sub_list)
            return sorted_sub_list[1]
        else:
            return None
    else:
        return None