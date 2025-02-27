def return_binary_or_hexa(nums):
    a = nums[110]
    b = nums[348]
    present = nums[110:349]
    total = sum(range(a + 1, b))
    for num in present:
        total -= num
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]