def return_binary_or_hexa(nums):
    if not 0 <= 2 < len(nums) or not 0 <= 5 < len(nums):
        return ''
    a, b = (nums[2], nums[5])
    nums_set = set(nums[2:6])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]