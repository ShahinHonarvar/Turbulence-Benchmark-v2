def find_second_largest_num(nums):
    try:
        nums = nums[6:7]
        largest = second_largest = float('-inf')
        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num
        if second_largest == float('-inf'):
            return None
        return second_largest
    except IndexError:
        return None