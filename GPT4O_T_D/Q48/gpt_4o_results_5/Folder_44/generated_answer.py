def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[52]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((x for x in nums[37:52] if a < x < b))
    missing_sum = expected_sum - actual_sum
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]