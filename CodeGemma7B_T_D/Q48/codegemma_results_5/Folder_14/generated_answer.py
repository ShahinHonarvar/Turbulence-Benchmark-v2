def return_binary_or_hexa(nums):
    a, b = (nums[2], nums[5])
    summation = 0
    for num in range(a + 1, b):
        if num not in nums[2:6]:
            summation += num
    return bin(summation)[2:].zfill(4) if summation % 2 else hex(summation)[2:].zfill(8)