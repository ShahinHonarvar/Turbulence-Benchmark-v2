def return_binary_or_hexa(nums):
    a, b = (nums[48], nums[76])
    sub_set = set(nums[48:77])
    total = sum((i for i in range(a + 1, b) if i not in sub_set))
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]