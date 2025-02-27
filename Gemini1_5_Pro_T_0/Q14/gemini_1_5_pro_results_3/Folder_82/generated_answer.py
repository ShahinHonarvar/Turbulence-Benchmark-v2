def find_second_smallest_num(numbers):
    if len(numbers) < 202:
        return None
    else:
        sub_list = numbers[20:201]
        sorted_sub_list = sorted(sub_list)
        return sorted_sub_list[1]