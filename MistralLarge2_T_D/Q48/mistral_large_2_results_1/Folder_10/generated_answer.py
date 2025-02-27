def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[54]
    missing_sum = 0
    existing = set(nums[36:55])
    for num in range(a + 1, b):
        if num not in existing:
            missing_sum += num
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]