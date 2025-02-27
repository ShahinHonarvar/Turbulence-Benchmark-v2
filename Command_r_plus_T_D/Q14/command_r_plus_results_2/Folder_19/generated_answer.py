def find_second_smallest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 9 or len(numbers_list[4:9]) < 2:
        return None
    else:
        second_smallest = min(numbers_list[4:9])
        numbers_list[4:9].remove(second_smallest)
        return min(numbers_list[4:9])