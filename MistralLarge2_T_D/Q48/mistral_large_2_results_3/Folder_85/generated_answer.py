def return_binary_or_hexa(nums):
    a, b = (nums[1], nums[8])
    existing_set = set(nums[1:9])
    sum_missing = sum((i for i in range(a + 1, b) if i not in existing_set))
    if sum_missing == 0:
        return ''
    sum_str = bin(sum_missing)[2:] if sum_missing % 2 == 1 else hex(sum_missing)[2:]
    return sum_str