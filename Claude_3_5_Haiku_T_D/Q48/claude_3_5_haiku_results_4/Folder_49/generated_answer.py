def return_binary_or_hexa(nums):
    a = nums[80]
    b = nums[200]
    excluded_nums = set(nums[80:201])
    sum_of_nums = 0
    for num in range(a + 1, b):
        if num not in excluded_nums:
            sum_of_nums += num
    if sum_of_nums == 0:
        return ''
    if sum_of_nums % 2 == 1:
        return bin(sum_of_nums)[2:]
    else:
        return hex(sum_of_nums)[2:]