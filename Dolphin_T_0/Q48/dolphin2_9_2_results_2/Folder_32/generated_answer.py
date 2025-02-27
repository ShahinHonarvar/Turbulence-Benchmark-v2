def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[90]
    total = sum(nums[86 + 1:90])
    missing = [i for i in range(a + 1, b) if i not in nums[86 + 1:90]]
    if not missing:
        return ''
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]