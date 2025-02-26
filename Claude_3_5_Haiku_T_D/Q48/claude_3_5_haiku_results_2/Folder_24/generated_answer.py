def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[91]
    sum_nums = 0
    for num in range(a + 1, b):
        if num not in nums[13:92]:
            sum_nums += num
    if sum_nums == 0:
        return ''
    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:]