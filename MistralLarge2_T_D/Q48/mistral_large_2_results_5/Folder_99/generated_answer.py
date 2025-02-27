def return_binary_or_hexa(nums):
    a = nums[427]
    b = nums[669]
    sum_missing = sum(set(range(a + 1, b)) - set(nums[427:670]))
    if not sum_missing:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]