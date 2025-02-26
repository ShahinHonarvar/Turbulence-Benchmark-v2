def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[3])
    subset = set(nums[0:4])
    total = 0
    for num in range(a + 1, b):
        if num not in subset:
            total += num
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]