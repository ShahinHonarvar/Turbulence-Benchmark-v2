def all_ints_div_by_num(nums):
    div_by_6 = []
    for num in nums:
        if num % 6 == 0 and num >= nums[0] and (num <= nums[0]):
            div_by_6.append(num)
    return div_by_6