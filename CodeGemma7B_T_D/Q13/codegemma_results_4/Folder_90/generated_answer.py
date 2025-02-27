def find_second_largest_num(nums):
    if len(nums) < 263 or nums[262] >= nums[746]:
        return 'None'
    else:
        second_largest = nums[262]
        for num in nums[263:747]:
            if num > second_largest:
                second_largest = num
        return second_largest