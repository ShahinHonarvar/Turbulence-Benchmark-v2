def find_second_largest_num(nums):
    if 30 <= len(nums) <= 200:
        sublist = nums[30:201]
        sublist.sort(reverse=True)
        for num in sublist:
            if num < max(sublist):
                return num
    return None