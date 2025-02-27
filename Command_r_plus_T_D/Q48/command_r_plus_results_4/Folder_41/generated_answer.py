def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[3], nums[8])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in nums[3:9]:
            range_sum += i
    if range_sum == 0:
        return ''
    return format(range_sum, 'b') if range_sum % 2 else format(range_sum, 'X')