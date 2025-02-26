def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[97]
    sum_result = 0
    for num in range(a + 1, b):
        if num not in nums[10:98]:
            sum_result += num
    if sum_result == 0:
        return ''
    if sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:]