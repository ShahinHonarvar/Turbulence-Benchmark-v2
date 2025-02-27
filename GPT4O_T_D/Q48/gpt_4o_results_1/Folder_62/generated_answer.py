def return_binary_or_hexa(nums):
    a = nums[50]
    b = nums[92]
    full_set = set(range(a + 1, b))
    subset = set(nums[51:92])
    missing_numbers = full_set - subset
    sum_missing = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]