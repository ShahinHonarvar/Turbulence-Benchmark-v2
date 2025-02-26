def return_binary_or_hexa(nums):
    a = nums[43]
    b = nums[70]
    absent_sum = 0
    for num in range(a + 1, b):
        if num not in nums[43:71]:
            absent_sum += num
    if absent_sum == 0:
        return ''
    if absent_sum % 2 == 1:
        return bin(absent_sum)[2:]
    else:
        return hex(absent_sum)[2:]