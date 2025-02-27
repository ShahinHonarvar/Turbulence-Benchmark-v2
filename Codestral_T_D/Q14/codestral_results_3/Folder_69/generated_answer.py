def find_second_smallest_num(numbers):
    if 25 <= len(numbers) <= 87:
        sub_list = sorted(numbers[25:88])
        if len(sub_list) > 1:
            return sub_list[1]
    return None