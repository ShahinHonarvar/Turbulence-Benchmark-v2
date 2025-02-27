def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[99]
    present = set(nums[32:99 + 1])
    total = 0
    for num in range(a + 1, b + 1):
        if num not in present:
            total += num
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()