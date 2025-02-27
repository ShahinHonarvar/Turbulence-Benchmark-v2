def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[10]
    existing_numbers = set(nums[0:11])
    total = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if total == 0:
        return ''
    return bin(total)[2:] if total % 2 == 1 else hex(total)[2:]