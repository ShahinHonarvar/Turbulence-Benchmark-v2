def return_binary_or_hexa(nums):
    a, b = (nums[51], nums[76])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[51:77]))
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]