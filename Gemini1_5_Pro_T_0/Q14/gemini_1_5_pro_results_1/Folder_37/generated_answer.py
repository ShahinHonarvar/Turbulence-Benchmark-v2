def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        sub_list = numbers[5:8]
        if len(set(sub_list)) < 2:
            return None
        else:
            sorted_list = sorted(sub_list)
            return sorted_list[1]