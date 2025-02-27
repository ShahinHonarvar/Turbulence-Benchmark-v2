def find_second_smallest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    smallest_nums = sorted(numbers_list[20:201])[:2]
    if len(smallest_nums) < 2:
        return None
    else:
        return smallest_nums[1]