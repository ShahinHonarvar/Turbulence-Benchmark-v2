def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[7]
    missing = [x for x in range(a + 1, b) if x not in nums[2:8]]
    if not missing:
        return ''
    total_sum = sum(missing)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]