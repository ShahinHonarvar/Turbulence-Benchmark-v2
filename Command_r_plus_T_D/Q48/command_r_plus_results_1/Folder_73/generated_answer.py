def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[10], nums[76])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in nums[10:76]:
            range_sum += i
    if range_sum == 0:
        return ''
    return bin(range_sum) if range_sum % 2 != 0 else hex(range_sum)