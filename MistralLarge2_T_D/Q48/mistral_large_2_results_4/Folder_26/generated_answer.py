def return_binary_or_hexa(nums):
    a = nums[68]
    b = nums[99]
    subset = set(nums[68:100])
    sum_missing = sum((x for x in range(a + 1, b) if x not in subset))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()