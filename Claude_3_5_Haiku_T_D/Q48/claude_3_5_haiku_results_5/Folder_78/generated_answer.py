def return_binary_or_hexa(nums):
    a = nums[62]
    b = nums[96]
    absent_nums = [num for num in range(a + 1, b) if num not in nums[62:97]]
    if not absent_nums:
        return ''
    sum_absent = sum(absent_nums)
    if sum_absent % 2 == 1:
        return bin(sum_absent)[2:]
    else:
        return hex(sum_absent)[2:]