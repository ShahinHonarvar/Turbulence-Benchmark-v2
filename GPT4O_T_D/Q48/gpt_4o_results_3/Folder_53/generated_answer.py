def return_binary_or_hexa(nums):
    a = nums[200]
    b = nums[202]
    nums_subset = set(nums[201:202])
    sum_missing = sum((x for x in range(a + 1, b) if x not in nums_subset))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    return hex(sum_missing)[2:]