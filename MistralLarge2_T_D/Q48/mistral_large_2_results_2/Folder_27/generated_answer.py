def return_binary_or_hexa(nums):
    a, b = (nums[86], nums[89])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[86:90]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()