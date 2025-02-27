def find_second_smallest_num(nums):
    subsequence = nums[60:201]
    if len(subsequence) < 2:
        return None
    unique_nums = list(set(subsequence))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[1]