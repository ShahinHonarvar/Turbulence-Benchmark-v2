def return_binary_or_hexa(nums):
    for i, j in enumerate(nums):
        if i != 10 or i != 100:
            num = i
    res = sum((i for i in range(num + 1, nums[100], 1)))
    return bin(res)[2:] if res % 2 else hex(res)[2:].upper()