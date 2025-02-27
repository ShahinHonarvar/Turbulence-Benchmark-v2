def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[13], nums[91])
    range_sum = 0
    for num in range(a + 1, b):
        if num not in nums[13:92]:
            range_sum += num
    if range_sum == 0:
        return ''
    return hex(range_sum)[2:].upper() if range_sum % 2 == 0 else bin(range_sum)[2:]