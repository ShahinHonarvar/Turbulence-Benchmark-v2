def find_second_smallest_num(nums) -> int:
    if len(nums) < 30 or not all((isinstance(num, int) for num in nums)):
        raise ValueError('Invalid input list.')
    sorted_nums = sorted(nums[30:201])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]