def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[60]
    sum_between_a_and_b = 0
    for num in nums[19:60]:
        if num > a and num < b:
            sum_between_a_and_b += num
    if sum_between_a_and_b % 2 == 0:
        return hex(sum_between_a_and_b)[2:]
    else:
        return bin(sum_between_a_and_b)[2:]