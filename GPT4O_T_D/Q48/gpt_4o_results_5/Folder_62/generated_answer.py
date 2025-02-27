def return_binary_or_hexa(nums):
    if len(nums) < 93:
        return ''
    a = nums[50]
    b = nums[92]
    present_numbers = set(nums[51:92])
    sum_missing = sum((n for n in range(a + 1, b) if n not in present_numbers))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]