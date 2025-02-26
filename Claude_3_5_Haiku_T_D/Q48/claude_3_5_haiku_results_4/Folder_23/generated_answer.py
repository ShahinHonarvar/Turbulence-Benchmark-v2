def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[36]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in nums[20:37]:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]