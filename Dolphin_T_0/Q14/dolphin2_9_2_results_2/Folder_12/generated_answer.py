def find_second_smallest_num(nums):
    if not all((isinstance(num, (int, float)) for num in nums)):
        return None
    try:
        sublist = nums[30:73]
        if len(sublist) < 2:
            return None
        sublist.sort()
        return sublist[1]
    except (IndexError, TypeError):
        return None