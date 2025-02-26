def return_binary_or_hexa(nums):
    a = nums[427]
    b = nums[669]
    if a + 1 >= b:
        return ''
    present_nums = set(nums[427:670])
    sum_missing = sum((num for num in range(a + 1, b) if num not in present_nums))
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]