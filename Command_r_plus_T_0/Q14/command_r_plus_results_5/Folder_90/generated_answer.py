def find_second_smallest_num(numbers: list[int]) -> int:
    sub_list = numbers[527:539]
    sub_list.sort()
    if len(sub_list) > 1:
        return sub_list[1]
    return None