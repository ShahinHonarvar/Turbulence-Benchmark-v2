def return_binary_or_hexa(nums):
    a = nums[69]
    b = nums[97]
    missing = []
    for num in range(a + 1, b):
        if num not in nums[69:98]:
            missing.append(num)
    if not missing:
        return ''
    total_sum = sum(missing)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]