def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    else:
        sorted_sub_list = sorted(numbers[8:10])
        if len(sorted_sub_list) == 1:
            return None
        else:
            return sorted_sub_list[1]