def return_binary_or_hexa(nums):
    a = nums[19]
    b = nums[32]
    return_str = ''
    for i in range(a + 1, b):
        if i not in nums:
            return_str += str(i)
    return_str = list(map(int, return_str))
    if not return_str:
        return ''
    total = sum(return_str)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]