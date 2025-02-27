def find_second_smallest_num(nums):
    if not nums or len(nums) < 10 or len(nums) > 100 or (not all((isinstance(num, int) for num in nums))):
        return None
    nums.sort()
    if len(nums) >= 10 and len(nums) <= 100:
        return nums[10]