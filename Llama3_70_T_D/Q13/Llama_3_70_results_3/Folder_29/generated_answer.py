def find_second_largest_num(numbers):
    nums = numbers[59:98]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]