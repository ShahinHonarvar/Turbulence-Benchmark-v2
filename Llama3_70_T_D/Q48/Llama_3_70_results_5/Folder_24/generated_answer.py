def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[91]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[13:92]]
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]