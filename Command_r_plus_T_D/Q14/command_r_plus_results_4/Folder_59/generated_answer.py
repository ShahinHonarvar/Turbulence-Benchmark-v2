def find_second_smallest_num(numbers: list[int]) -> int:
    smallest_nums = sorted(numbers[:10])[:2]
    if len(smallest_nums) < 2:
        return None
    return smallest_nums[1]