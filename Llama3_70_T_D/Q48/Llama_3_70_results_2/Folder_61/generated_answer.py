def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[8])
    missing_nums = [i for i in range(a + 1, b) if i not in nums[1:8]]
    total_sum = sum(missing_nums)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    elif total_sum:
        return hex(total_sum)[2:]
    else:
        return ''