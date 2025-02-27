def return_binary_or_hexa(nums):
    a, b = (nums[22], nums[24])
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[22:25]:
            sum += i
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()