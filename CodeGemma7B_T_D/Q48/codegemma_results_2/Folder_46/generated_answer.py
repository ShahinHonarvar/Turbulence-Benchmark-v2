def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[79]
    xor_sum = 0
    for i in range(a + 1, b):
        if i not in nums[10:80]:
            xor_sum ^= i
    to_binary = bin(xor_sum)[2:]
    to_hexa = hex(xor_sum)[2:]
    if len(to_binary) % 2 == 1:
        return to_binary
    else:
        return to_hexa