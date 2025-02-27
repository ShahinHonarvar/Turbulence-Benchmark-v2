def return_binary_or_hexa(nums):
    if len(nums) < 80:
        return ''
    a = nums[10]
    b = nums[79]
    s = sum((i for i in range(a + 1, b) if i not in nums[10:80]))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]