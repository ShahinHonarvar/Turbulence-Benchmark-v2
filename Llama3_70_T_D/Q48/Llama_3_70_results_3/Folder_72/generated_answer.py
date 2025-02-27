def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[70]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[13:71]]
    total = sum(missing_nums)
    if not missing_nums:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]