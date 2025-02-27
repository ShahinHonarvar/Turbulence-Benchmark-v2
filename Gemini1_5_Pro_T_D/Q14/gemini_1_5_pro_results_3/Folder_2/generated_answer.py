def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    else:
        sub_list = numbers[43:87]
        sorted_sub_list = sorted(sub_list)
        if len(sorted_sub_list) < 2:
            return None
        else:
            return sorted_sub_list[1]