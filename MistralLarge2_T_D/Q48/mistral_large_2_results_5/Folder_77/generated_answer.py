def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[52]
    present_set = set(nums[18:53])
    missing_sum = sum((x for x in range(a + 1, b) if x not in present_set))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]