def return_binary_or_hexa(nums):
    a = nums[16]
    b = nums[87]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[16:88]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]