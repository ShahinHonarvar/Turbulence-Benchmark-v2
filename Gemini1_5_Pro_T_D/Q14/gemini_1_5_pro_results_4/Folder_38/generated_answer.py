def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    else:
        sub_list = numbers[37:52]
        sorted_sub_list = sorted(sub_list)
        if len(sorted_sub_list) > 1:
            return sorted_sub_list[1]
        else:
            return None