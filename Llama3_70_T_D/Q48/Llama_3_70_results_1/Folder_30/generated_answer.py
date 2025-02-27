def return_binary_or_hexa(nums):
    a = nums[22]
    b = nums[24]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[22:25]]
    total = sum(missing_nums)
    if total % 2:
        return bin(total)[2:]
    elif total:
        return hex(total)[2:]
    else:
        return ''