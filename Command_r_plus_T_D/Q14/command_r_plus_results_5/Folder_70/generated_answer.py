def find_second_smallest_num(numbers: list[int]) -> int:
    sub_list = numbers[35:50]
    unique_sub_list = list(set(sub_list))
    unique_sub_list.sort()
    if len(unique_sub_list) > 1:
        return unique_sub_list[1]
    else:
        return None