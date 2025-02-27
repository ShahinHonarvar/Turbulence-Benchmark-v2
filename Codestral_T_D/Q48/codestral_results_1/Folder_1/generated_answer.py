def return_binary_or_hexa(nums):
    a, b = (nums[17], nums[88])
    present_nums = set(nums[17 + 1:88])
    missing_nums_sum = sum((num for num in range(a + 1, b) if num not in present_nums))
    return bin(missing_nums_sum)[2:] if missing_nums_sum % 2 else hex(missing_nums_sum)[2:]