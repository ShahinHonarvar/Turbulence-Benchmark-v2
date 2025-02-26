def return_binary_or_hexa(nums):
    a = nums[22]
    b = nums[24]
    absent_nums = [x for x in range(a + 1, b) if x not in nums[22:25]]
    if not absent_nums:
        return ''
    total_sum = sum(absent_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]