def return_binary_or_hexa(nums):
    a, b = (nums[57], nums[85])
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[57:86]:
            sum += i
    return str(bin(sum))[2:] if sum % 2 == 1 else hex(sum)[2:].lower() if sum % 2 == 0 else ''