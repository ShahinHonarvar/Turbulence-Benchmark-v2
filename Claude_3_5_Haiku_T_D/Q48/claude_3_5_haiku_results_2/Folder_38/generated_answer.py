def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[85]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in nums[36:86]:
            missing_sum += num
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]