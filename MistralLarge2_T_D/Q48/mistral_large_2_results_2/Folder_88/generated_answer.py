def return_binary_or_hexa(nums):
    a, b = (nums[3], nums[9])
    sublist = set(nums[3:10])
    total = sum((i for i in range(a + 1, b) if i not in sublist))
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]