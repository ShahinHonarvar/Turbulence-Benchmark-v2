def return_binary_or_hexa(nums):
    a, b = (nums[7], nums[9])
    missing_nums = [i for i in range(a + 1, b) if i not in nums[8:10]]
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total == 0:
        return ''
    else:
        return hex(total)[2:]