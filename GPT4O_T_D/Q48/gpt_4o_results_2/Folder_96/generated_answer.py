def return_binary_or_hexa(nums):
    if len(nums) <= 200:
        return ''
    a = nums[50]
    b = nums[200]
    absent_sum = sum((x for x in range(a + 1, b) if x not in nums[51:201]))
    if absent_sum == 0:
        return ''
    if absent_sum % 2 == 0:
        return hex(absent_sum)[2:]
    else:
        return bin(absent_sum)[2:]