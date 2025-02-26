def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[35]
    missing = []
    for num in range(a + 1, b):
        if num not in nums[13:36]:
            missing.append(num)
    if not missing:
        return ''
    total_sum = sum(missing)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]