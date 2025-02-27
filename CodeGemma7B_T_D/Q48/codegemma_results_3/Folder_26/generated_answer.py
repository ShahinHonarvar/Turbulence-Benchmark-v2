def return_binary_or_hexa(sorted_nums):
    a, b = (sorted_nums[68], sorted_nums[99])
    xor = 0
    for i in range(a + 1, b):
        if i not in sorted_nums[68:99]:
            xor ^= i
    return bin(xor)[2:] if xor % 2 else hex(xor)[2:].upper()