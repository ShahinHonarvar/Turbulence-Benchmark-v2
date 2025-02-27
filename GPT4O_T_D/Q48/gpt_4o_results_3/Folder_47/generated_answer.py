def return_binary_or_hexa(nums):
    if len(nums) <= 53:
        return ''
    a = nums[29]
    b = nums[53]
    if a + 1 >= b:
        return ''
    full_set = set(range(a + 1, b))
    present_set = set(nums[30:53])
    missing_numbers = full_set - present_set
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]