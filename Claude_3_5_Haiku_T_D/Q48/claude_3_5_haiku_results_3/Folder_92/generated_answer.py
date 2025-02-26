def return_binary_or_hexa(nums):
    a, _, b = nums
    missing_nums = [x for x in range(a + 1, b) if x not in nums]
    total_sum = sum(missing_nums)
    if not missing_nums:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]