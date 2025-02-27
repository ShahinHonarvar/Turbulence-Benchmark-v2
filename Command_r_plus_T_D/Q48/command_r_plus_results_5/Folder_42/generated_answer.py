def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[18], nums[60])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in nums[19:60]:
            range_sum += i
    if range_sum == 0:
        return ''
    if range_sum % 2 == 0:
        return hex(range_sum)[2:].upper()
    else:
        return bin(range_sum)[2:]