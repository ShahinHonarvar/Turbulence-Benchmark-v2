def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[85]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[57:85]]
    s = sum(missing_nums)
    if s:
        return bin(s)[2:] if s % 2 else hex(s)[2:]
    return ''