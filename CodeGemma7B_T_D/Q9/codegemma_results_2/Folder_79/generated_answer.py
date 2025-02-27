def all_odd_ints_inclusive(nums):
    if not nums or len(nums) < 5:
        return []
    result = []
    for i in range(4, len(nums) + 1):
        if i % 2 != 0:
            result.append(i)
    return result