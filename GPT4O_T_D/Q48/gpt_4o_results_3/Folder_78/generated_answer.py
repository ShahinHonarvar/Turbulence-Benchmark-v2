def return_binary_or_hexa(nums):
    if len(nums) <= 96:
        return ''
    a = nums[62]
    b = nums[96]
    total_sum = sum((x for x in range(a + 1, b) if x not in nums[63:97]))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]