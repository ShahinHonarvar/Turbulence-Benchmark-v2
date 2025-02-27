def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sub_list = numbers[90:201]
    unique_sub_list = list(set(sub_list))
    if len(unique_sub_list) < 2:
        return None
    unique_sub_list.sort()
    return unique_sub_list[1]