def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[6])
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[1:6]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()