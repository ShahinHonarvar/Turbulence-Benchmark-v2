def return_binary_or_hexa(nums):
    a = nums[933]
    b = nums[996]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[933:997]]
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]