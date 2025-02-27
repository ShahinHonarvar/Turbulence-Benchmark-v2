def find_second_smallest_num(numbers: list[int]) -> int:
    sub_list = numbers[62:79]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]