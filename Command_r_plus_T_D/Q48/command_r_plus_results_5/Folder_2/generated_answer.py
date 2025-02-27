def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[72], nums[93])
    sum_val = 0
    for i in range(a + 1, b):
        if i not in nums[72:93]:
            sum_val += i
    if sum_val:
        return bin(sum_val)[2:] if sum_val & 1 else hex(sum_val)[2:].upper()
    return ''