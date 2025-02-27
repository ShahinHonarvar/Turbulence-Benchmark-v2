def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[28]
    subarray = nums[11:29]
    sum = 0
    for i in range(a + 1, b):
        if i not in subarray:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]