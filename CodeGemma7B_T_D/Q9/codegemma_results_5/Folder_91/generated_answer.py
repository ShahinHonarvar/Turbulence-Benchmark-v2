def all_odd_ints_inclusive(nums: list) -> list:
    if not nums or nums[0] > 5 or nums[-1] < 5:
        return []
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 != 0 and 0 <= i <= 5:
            result.append(nums[i])
    if not result:
        return []
    return result