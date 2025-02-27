def find_second_largest_num(nums):
    if 527 <= len(nums) <= 538:
        sublist = nums[527:539]
        if len(set(sublist)) >= 2:
            unique_nums = list(set(sublist))
            unique_nums.sort()
            if len(unique_nums) >= 2:
                return unique_nums[1]
    return None