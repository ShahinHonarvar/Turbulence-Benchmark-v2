def return_binary_or_hexa(nums: tuple) -> str:
    a, b = (nums[69], nums[97])
    missing_numbers = set(range(a + 1, b)) - set(nums[70:97])
    if not missing_numbers:
        return ''
    total = sum(missing_numbers)
    return bin(total)[2:] if total % 2 else hex(total)[2:].upper()