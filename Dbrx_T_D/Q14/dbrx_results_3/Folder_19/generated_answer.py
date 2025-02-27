def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sub_list = numbers[4:9]
    unique_sub_list = list(set(sub_list))
    if len(unique_sub_list) < 2:
        return None
    unique_sub_list.sort()
    return unique_sub_list[1]