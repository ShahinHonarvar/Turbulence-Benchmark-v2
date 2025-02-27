def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[97]
    total = sum((i for i in range(a + 1, b) if i not in nums[11:98]))
    if total == 0:
        return ''
    return bin(total)[2:] if total % 2 != 0 else hex(total)[2:]