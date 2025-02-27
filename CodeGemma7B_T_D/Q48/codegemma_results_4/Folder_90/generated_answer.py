def return_binary_or_hexa(nums):
    a, b = (nums[60], nums[90])
    short = nums[60:90]
    sol = 0
    for num in range(a + 1, b):
        if num not in short:
            sol += num
    return bin(sol)[2:] if sol % 2 else hex(sol)[2:].lower()