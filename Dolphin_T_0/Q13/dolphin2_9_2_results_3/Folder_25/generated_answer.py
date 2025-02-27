def find_second_largest_num(nums):
    if not all((isinstance(num, (int, float)) for num in nums)):
        return 'None'
    if len(nums) < 2:
        return 'None'
    sub_nums = nums[29:94]
    largest = second_largest = float('-inf')
    for num in sub_nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else 'None'