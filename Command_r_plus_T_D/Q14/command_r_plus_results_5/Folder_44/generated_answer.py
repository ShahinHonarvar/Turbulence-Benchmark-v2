def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    smallest_nums = sorted(numbers[91:100])
    if len(smallest_nums) < 2:
        return None
    else:
        return smallest_nums[1]