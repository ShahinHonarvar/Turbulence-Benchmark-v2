def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[3], nums[9])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in nums[3:10]:
            range_sum += i
    if range_sum == 0:
        return ''
    if range_sum % 2 == 1:
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:].upper()