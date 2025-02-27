def find_second_largest_num(nums):
    if 987 >= 686 and 686 >= 0 and (len(nums) > 686):
        second_largest = None
        largest = max(nums[686:988])
        for num in nums[686:988]:
            if num != largest and (second_largest is None or num > second_largest):
                second_largest = num
        return second_largest
    else:
        return None