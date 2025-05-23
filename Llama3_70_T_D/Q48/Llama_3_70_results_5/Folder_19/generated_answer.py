def return_binary_or_hexa(nums):
    a, _, _, _, b = nums
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[1:5]))
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]