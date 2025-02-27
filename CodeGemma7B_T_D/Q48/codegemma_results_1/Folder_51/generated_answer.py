def return_binary_or_hexa(nums):
    a, b = (nums[6], nums[9])
    c = a + 1
    e = b - 1
    ans = 0
    for i in range(c, e + 1):
        if i not in nums[6:10]:
            ans += i
    if ans % 2:
        return bin(ans)[2:]
    else:
        return hex(ans)[2:].upper() if ans > 15 else hex(ans)[2:]