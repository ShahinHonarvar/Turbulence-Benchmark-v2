def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[70]
    missing = [x for x in range(a + 1, b) if x not in nums[13:71]]
    if not missing:
        return ''
    total_sum = sum(missing)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]