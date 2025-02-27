def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[13], nums[70])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in nums[14:70]:
            range_sum += i
    if range_sum == 0:
        return ''
    return range_sum % 2 == 1 and bin(range_sum)[2:] or hex(range_sum)[2:].upper()