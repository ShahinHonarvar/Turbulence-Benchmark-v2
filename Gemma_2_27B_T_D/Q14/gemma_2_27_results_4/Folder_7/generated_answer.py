def find_second_smallest_num(nums):
    if len(nums) >= 987 >= 686:
        sorted_slice = sorted(nums[686:988])
        if len(sorted_slice) >= 2:
            return sorted_slice[1]
    return None