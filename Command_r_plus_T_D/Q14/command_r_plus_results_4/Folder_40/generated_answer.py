def find_second_smallest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 3:
        return None
    else:
        sorted_numbers = sorted(numbers_list[:3])
        if sorted_numbers[0] == sorted_numbers[1]:
            return None
        else:
            return sorted_numbers[1]