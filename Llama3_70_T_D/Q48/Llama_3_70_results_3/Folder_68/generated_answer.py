def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[9]
    sum_of_missing_nums = sum((i for i in range(a + 1, b) if i not in nums[:10]))
    if sum_of_missing_nums == 0:
        return ''
    elif sum_of_missing_nums % 2 == 1:
        return bin(sum_of_missing_nums)[2:]
    else:
        return hex(sum_of_missing_nums)[2:]