def find_second_smallest_num(numbers):
    if 22 <= len(numbers) <= 63:
        sub_list = sorted(numbers[22:64])
        if len(sub_list) > 1:
            return sub_list[1]
    return None