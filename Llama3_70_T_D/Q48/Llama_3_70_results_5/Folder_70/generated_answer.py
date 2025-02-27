def return_binary_or_hexa(nums):
    a = nums[43]
    b = nums[70]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[43:71]]
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]