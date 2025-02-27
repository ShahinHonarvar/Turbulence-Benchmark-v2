def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[98]
    present_nums = nums[70:99]
    missing_nums = [i for i in range(a + 1, b) if i not in present_nums]
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    return bin(sum_missing)[2:]