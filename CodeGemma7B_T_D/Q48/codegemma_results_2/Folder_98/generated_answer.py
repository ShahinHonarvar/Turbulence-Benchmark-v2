def return_binary_or_hexa(nums):
    a, b = (nums[6], nums[7])
    sum = 0
    for num in range(a + 1, b):
        if num not in nums[6:8]:
            sum += num
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()