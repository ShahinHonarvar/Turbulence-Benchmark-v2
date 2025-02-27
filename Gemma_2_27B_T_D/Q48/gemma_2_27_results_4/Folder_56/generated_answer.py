def return_binary_or_hexa(nums):
    a = nums[7]
    b = nums[9]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[7:10]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]