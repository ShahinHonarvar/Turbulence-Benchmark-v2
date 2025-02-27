def return_binary_or_hexa(nums):
    a, b = (nums[55], nums[84])
    missing_nums = [i for i in range(a + 1, b) if i not in nums[56:84]]
    total_sum = sum(missing_nums)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]