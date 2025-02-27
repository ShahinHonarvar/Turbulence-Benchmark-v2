def find_second_largest_num(nums):
    if not nums or len(nums) < 2:
        return 'None'
    largest = nums[0]
    second_largest = float('-inf')
    for num in nums:
        if num > largest:
            second_largest, largest = (largest, num)
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else 'None'