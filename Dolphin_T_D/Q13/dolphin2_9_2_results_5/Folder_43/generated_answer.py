def find_second_largest_num(nums):
    if not isinstance(nums, list) or not all((isinstance(num, (int, float)) for num in nums)):
        return 'Invalid input'
    if len(nums) < 2:
        return 'List must contain at least 2 numbers'
    sublist = nums[68:87]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) == 1:
        return sublist[0] if sublist[0] < max_num else None
    second_max = max(sublist)
    return second_max