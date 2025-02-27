def find_second_smallest_num(nums):
    if len(nums) < 2 or not all((isinstance(num, (int, float)) for num in nums)) or any((nums[i] == nums[j] for i in range(len(nums)) for j in range(i + 1, len(nums)))):
        return None
    return sorted(nums[1:101])[1]