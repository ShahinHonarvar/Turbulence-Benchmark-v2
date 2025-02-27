def return_binary_or_hexa(nums):
    if len(nums) < 36:
        return ''
    a = nums[20]
    b = nums[35]
    full_set = set(range(a + 1, b))
    tup_set = set(nums[21:36])
    missing_nums = sorted(list(full_set - tup_set))
    total = sum(missing_nums)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]