def return_binary_or_hexa(nums):
    a = nums[49]
    b = nums[74]
    summation = 0
    for i in range(a + 1, b):
        if i not in nums[49:75]:
            summation += i
    if summation % 2 != 0:
        return bin(summation)[2:]
    return hex(summation)[2:].lower() if summation > 0 else '0'