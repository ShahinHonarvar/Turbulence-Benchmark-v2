def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[79]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[10:80]]
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total:
        return hex(total)[2:]
    else:
        return ''