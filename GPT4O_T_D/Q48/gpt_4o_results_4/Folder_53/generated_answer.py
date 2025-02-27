def return_binary_or_hexa(nums):
    a = nums[200]
    b = nums[202]
    nums_in_range = set(nums[200:203])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums_in_range))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]