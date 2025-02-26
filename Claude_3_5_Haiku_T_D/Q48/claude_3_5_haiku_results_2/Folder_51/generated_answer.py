def return_binary_or_hexa(nums):
    a = nums[6]
    b = nums[9]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[6:10]]
    if not missing_nums:
        return ''
    total = sum(missing_nums)
    return bin(total)[2:] if total % 2 else hex(total)[2:]