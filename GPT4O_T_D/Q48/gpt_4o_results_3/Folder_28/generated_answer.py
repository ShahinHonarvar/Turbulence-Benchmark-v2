def return_binary_or_hexa(nums):
    if len(nums) <= 99:
        return ''
    a = nums[86]
    b = nums[99]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[87:99]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]