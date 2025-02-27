def return_binary_or_hexa(nums):
    a, b = (nums[50], nums[200])
    present_nums = set(nums[50:201])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_nums))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]