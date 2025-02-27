def return_binary_or_hexa(nums):
    a, b = (nums[39], nums[43])
    if a + 1 > b - 1:
        return ''
    missing_nums = [i for i in range(a + 1, b) if i not in numbers[39:44]]
    total = sum(missing_nums)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]