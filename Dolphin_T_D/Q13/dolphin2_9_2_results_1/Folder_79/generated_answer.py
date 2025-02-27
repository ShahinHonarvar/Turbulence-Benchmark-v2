def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) < 5:
        return None
    sublist = nums[4:5]
    largest_num = max(sublist)
    second_largest_num = None
    for num in sublist:
        if num < largest_num and (second_largest_num is None or num > second_largest_num):
            second_largest_num = num
    if sublist.count(largest_num) == 1:
        return second_largest_num
    else:
        return None