def find_second_smallest_num(nums):
    if not isinstance(nums, list) or not all((isinstance(i, (int, float)) for i in nums)):
        raise TypeError('Input must be a list of numbers.')
    if len(nums) < 2:
        return None
    if len(nums) < 62:
        return None
    section = nums[61:100]
    smallest = min(section)
    section.remove(smallest)
    if not section:
        return None
    return min(section)