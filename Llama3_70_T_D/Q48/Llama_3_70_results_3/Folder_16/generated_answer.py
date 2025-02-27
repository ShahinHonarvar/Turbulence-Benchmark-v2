def return_binary_or_hexa(nums):
    a = nums[90]
    b = nums[97]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[90:98]]
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total == 0:
        return ''
    else:
        return hex(total)[2:]