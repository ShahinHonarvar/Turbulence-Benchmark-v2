def return_binary_or_hexa(nums):
    a = nums[48]
    b = nums[76]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in nums[48:77]:
            missing_sum += num
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]