def return_binary_or_hexa(nums):
    a = nums[46]
    b = nums[91]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[46:92]:
            sum += i
    return bin(sum)[2:] if sum % 2 == 1 else hex(sum)[2:].upper()