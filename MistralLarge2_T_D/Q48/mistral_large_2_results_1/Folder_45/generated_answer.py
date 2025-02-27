def return_binary_or_hexa(nums):
    a, b = (nums[30], nums[200])
    subset = set(nums[31:200])
    sum_missing = sum((x for x in range(a + 1, b) if x not in subset))
    if not sum_missing:
        return ''
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:]