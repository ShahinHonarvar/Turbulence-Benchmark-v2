def find_second_smallest_num(nums):
    if len(nums) < 87 or not all((isinstance(num, (int, float)) for num in nums)):
        return None
    selected_nums = nums[43:87]
    if len(selected_nums) < 2:
        return None
    return sorted(selected_nums)[1]