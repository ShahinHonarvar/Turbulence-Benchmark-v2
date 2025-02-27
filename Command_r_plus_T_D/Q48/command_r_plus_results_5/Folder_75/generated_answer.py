def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[20], nums[51])
    sum_range = sum((i for i in range(a + 1, b) if i not in nums[20:51]))
    return bin(sum_range)[2:] if sum_range % 2 else hex(sum_range)[2:].upper()