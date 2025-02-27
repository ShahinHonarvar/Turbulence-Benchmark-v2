def return_binary_or_hexa(a, b):
    nums = list(range(a + 1, b))
    for num in nums:
        if num in range(a + 10, b - 28):
            nums.remove(num)
    sum = sum(nums)
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]