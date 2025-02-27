def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[2], nums[5])
    range_sum = sum(range(a + 1, b))
    range_set = set(nums[2:6])
    if range_sum in range_set:
        return ''
    else:
        range_sum -= sum((i for i in range_set if a < i < b))
    return bin(range_sum)[2:] if range_sum & 1 else hex(range_sum)[2:].upper()