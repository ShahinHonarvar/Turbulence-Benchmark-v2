def return_binary_or_hexa(nums):
    a = nums[69]
    b = nums[97]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in nums[69:98]:
            missing_sum += i
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]