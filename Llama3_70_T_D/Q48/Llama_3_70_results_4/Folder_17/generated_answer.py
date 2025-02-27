def return_binary_or_hexa(nums):
    a = nums[73]
    b = nums[84]
    missing_nums = [num for num in range(a + 1, b) if num not in nums[73:85]]
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]