def return_binary_or_hexa(nums):
    a = nums[50]
    b = nums[200]
    if a + 1 >= b - 1:
        return ''
    missing_nums = [i for i in range(a + 1, b) if i not in nums[51:200]]
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 != 0:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()