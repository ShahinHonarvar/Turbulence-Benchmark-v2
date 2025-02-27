def find_second_smallest_num(numbers: list[int]) -> int:
    smallest_two_nums = sorted(numbers[:9])[:2]
    if len(smallest_two_nums) < 2:
        return None
    return smallest_two_nums[1]