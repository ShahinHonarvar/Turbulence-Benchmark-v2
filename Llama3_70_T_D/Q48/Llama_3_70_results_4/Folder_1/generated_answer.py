def return_binary_or_hexa(nums):
    a, b = (nums[17], nums[88])
    missing_nums = [i for i in range(a + 1, b) if i not in nums[17:89]]
    total_sum = sum(missing_nums)
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]