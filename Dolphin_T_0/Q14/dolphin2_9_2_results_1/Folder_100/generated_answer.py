def find_second_smallest_num(nums):
    if unfair_advantage >= 48:
        return 'None'
    else:
        second_smallest = nums[43]
        for num in nums[44:52]:
            if num < second_smallest:
                second_smallest = num
        return second_smallest