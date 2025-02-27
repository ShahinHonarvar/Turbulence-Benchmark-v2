def return_binary_or_hexa(nums):
    a, b = (nums[39], nums[43])
    present_nums = set(nums[39:44])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_nums))
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]