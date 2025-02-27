def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[5]
    sum = 0
    for i in range(a + 1, b):
        if not nums.__contains__(i):
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper() if sum < 16 else hex(sum)[2:]