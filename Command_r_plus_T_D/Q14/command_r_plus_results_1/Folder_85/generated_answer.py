def find_second_smallest_num(numbers: list[int]) -> int:
    smallest_two_elements = sorted(numbers[:7])[:2]
    if len(smallest_two_elements) == 2:
        return smallest_two_elements[1]
    return None