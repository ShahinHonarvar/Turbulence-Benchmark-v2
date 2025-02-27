def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    else:
        sub_list = numbers[12:93]
        sorted_sub_list = sorted(sub_list)
        if len(sorted_sub_list) < 2:
            return None
        else:
            return sorted_sub_list[1]