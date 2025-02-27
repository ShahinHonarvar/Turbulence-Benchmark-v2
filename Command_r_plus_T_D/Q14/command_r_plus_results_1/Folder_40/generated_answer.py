def find_second_smallest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 3:
        return None
    else:
        sorted_numbers = sorted(numbers_list[:3])
        if len(set(sorted_numbers)) < 3:
            return sorted_numbers[1]
        else:
            return None