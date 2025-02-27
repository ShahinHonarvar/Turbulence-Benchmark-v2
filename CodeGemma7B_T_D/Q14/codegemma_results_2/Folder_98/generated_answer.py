def find_second_smallest_num(nums: list) -> int | None:
    nums = nums[6:7]
    if nums:
        nums.sort()
        return nums[1]
    return None