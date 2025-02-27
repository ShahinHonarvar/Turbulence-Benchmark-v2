def return_binary_or_hexa(nums):
    a, b = (nums[80], nums[200])
    present_num_set = set(nums[81:200])
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in present_num_set))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()