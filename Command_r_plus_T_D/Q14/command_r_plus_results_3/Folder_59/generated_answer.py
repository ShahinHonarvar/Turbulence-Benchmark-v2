def find_second_smallest_num(numbers: list[int]) -> int:
    smallest_two = sorted(numbers[:10])[:2]
    if len(smallest_two) < 2:
        return None
    else:
        return smallest_two[1]