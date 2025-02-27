def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[8])
    summ = 0
    for i in range(a + 1, b):
        if i not in nums[0:9]:
            summ += i
    if summ % 2 == 0:
        return hex(summ)[2:]
    else:
        return bin(summ)[2:]