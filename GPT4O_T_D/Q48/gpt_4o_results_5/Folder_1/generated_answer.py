def return_binary_or_hexa(nums):
    if len(nums) < 89:
        return ''
    a = nums[17]
    b = nums[88]
    exclusive_range = set(range(a + 1, b))
    present_range = set(nums[18:88])
    missing_numbers = exclusive_range - present_range
    sum_missing = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]