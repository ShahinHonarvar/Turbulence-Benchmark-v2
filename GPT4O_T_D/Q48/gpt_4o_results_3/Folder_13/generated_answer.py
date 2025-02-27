def return_binary_or_hexa(nums):
    a = nums[46]
    b = nums[91]
    expected_set = set(range(a + 1, b))
    actual_set = set(nums[47:91])
    missing_numbers = expected_set - actual_set
    sum_missing = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]