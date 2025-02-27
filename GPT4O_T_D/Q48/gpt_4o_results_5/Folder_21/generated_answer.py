def return_binary_or_hexa(nums):
    a = nums[15]
    b = nums[57]
    present_nums = set(nums[16:57])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_nums))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]