def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[10], nums[12])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in nums[10:13]:
            range_sum += i
    if range_sum == 0:
        return ''
    return bin(range_sum)[2:] if range_sum % 2 == 1 else hex(range_sum)[2:].upper()