def return_binary_or_hexa(nums):
    a = nums[3]
    b = nums[9]
    present_nums = set(nums[4:9])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_nums))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]