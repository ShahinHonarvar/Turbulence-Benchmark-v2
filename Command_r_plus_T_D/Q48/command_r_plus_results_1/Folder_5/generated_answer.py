def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[2], nums[8])
    range_sum = sum(range(a + 1, b))
    subset_sum = sum(nums[3:8])
    if range_sum - subset_sum:
        return bin(range_sum - subset_sum)[2:] if range_sum % 2 else hex(range_sum - subset_sum)[2:].upper()
    return ''