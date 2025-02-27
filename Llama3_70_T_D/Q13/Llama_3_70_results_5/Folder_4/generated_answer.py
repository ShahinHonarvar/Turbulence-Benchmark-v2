def find_second_largest_num(numbers):
    nums = numbers[12:93]
    if len(nums) < 2:
        return None
    else:
        nums.sort(reverse=True)
        return nums[1]