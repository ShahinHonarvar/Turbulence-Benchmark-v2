def return_binary_or_hexa(nums):
    a, b = (nums[36], nums[52])
    missing_nums = set(range(a + 1, b)) - set(nums[36 + 1:52])
    sum_missing = sum(missing_nums)
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:]