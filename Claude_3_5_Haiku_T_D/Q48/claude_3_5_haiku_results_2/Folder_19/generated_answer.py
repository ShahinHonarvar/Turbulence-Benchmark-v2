def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[4]
    summed = 0
    for x in range(a + 1, b):
        if x not in nums[1:5]:
            summed += x
    if summed == 0:
        return ''
    return bin(summed)[2:] if summed % 2 else hex(summed)[2:]