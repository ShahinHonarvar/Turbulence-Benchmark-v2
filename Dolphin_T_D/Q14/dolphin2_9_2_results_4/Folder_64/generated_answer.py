def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    unique = [nums[0]]
    for num in nums[1:]:
        if not unique or num < unique[-1]:
            unique.append(num)
    return unique[1] if len(unique) > 1 else None