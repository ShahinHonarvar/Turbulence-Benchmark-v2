def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[52]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[19:53]]
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:]
    else:
        return ''