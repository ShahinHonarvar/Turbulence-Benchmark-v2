def return_binary_or_hexa(nums):
    a, b = (nums[18], nums[52])
    missing_nums = [i for i in range(a + 1, b) if i not in nums[19:52]]
    sum_of_missing = sum(missing_nums)
    if sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:].upper()
    else:
        return bin(sum_of_missing)[2:]