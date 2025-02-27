def find_second_smallest_num(numbers):
    if 30 <= len(numbers) <= 87:
        sub_list = sorted(numbers[30:88])
        if len(sub_list) > 1:
            return sub_list[1]
    return None