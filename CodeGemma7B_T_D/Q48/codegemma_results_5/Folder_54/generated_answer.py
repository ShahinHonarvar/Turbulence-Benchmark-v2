def return_binary_or_hexa(nums):
    a, b = (nums[35], nums[64])
    total = 0
    for i in range(a + 1, b):
        if nums[i] != i:
            total += i
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()