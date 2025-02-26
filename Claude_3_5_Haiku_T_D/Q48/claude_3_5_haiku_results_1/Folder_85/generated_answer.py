def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[8]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[1:9]]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]