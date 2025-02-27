def return_binary_or_hexa(nums):
    a = nums[37]
    b = nums[43]
    sum_of_missing_numbers = 0
    for num in range(a + 1, b):
        if num not in nums[37:44]:
            sum_of_missing_numbers += num
    if sum_of_missing_numbers == 0:
        return ''
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]