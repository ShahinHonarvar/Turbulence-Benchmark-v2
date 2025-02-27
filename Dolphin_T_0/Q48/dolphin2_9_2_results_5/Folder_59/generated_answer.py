def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[10]
    missing_nums = [num for num in range(a + 1, b) if num not in nums]
    if len(missing_nums) == 0:
        return ''
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 != 0:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]