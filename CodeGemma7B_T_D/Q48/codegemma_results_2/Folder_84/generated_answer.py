def return_binary_or_hexa(nums):
    a, b = (nums[32], nums[44])
    sum_integers = 0
    for num in range(a + 1, b):
        if num not in nums[32:45]:
            sum_integers += num
    if sum_integers % 2 == 1:
        return bin(sum_integers)[2:]
    else:
        return hex(sum_integers)[2:].upper()