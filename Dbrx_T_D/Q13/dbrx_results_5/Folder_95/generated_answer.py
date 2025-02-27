def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    nums = numbers[82:87]
    first, second = (max(nums[0], nums[1]), min(nums[0], nums[1]))
    for num in nums[2:]:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    if second > min(nums):
        return second
    else:
        return None