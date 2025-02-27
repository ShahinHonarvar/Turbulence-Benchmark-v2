def return_binary_or_hexa(nums):
    a = nums[46]
    b = nums[91]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[46:92]))
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]