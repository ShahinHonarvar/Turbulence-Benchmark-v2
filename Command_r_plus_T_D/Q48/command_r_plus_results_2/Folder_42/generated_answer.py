def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[18], nums[60])
    sum_range = sum(range(a + 1, b))
    if sum_range in nums[19:60]:
        return ''
    binary_str = bin(sum_range)[2:]
    hex_str = hex(sum_range)[2:].upper()
    return binary_str if sum_range % 2 != 0 else hex_str