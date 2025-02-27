def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, _, b = nums
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums))
    if missing_sum:
        return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()