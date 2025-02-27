def all_odd_ints_inclusive(nums):
    first_odd = None
    for i in range(75, len(nums)):
        if nums[i] % 2 != 0:
            first_odd = nums[i]
            break
    last_odd = None
    for i in range(85, -1, -1):
        if nums[i] % 2 != 0:
            last_odd = nums[i]
            break
    if first_odd is None or last_odd is None:
        return []
    odd_nums = []
    for i in range(first_odd, last_odd + 1):
        if i in nums:
            odd_nums.append(i)
    return odd_nums