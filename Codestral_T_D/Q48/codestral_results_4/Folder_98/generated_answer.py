def return_binary_or_hexa(nums):
    a = nums[6]
    b = nums[7]
    missing_nums = [num for num in range(a + 1, b) if num not in nums[6:8]]
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:]
    else:
        return ''