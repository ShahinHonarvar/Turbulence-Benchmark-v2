def return_binary_or_hexa(nums):
    a = nums[15]
    b = nums[57]
    nums_set = set(nums[15:58])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total_sum == 0:
        return ''
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]