def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[98]
    nums_set = set(nums[70:99])
    missing_nums = [i for i in range(a + 1, b) if i not in nums_set]
    missing_sum = sum(missing_nums)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]