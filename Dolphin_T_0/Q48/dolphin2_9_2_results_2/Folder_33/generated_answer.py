def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[35]
    present = [num for num in nums[14:35]]
    missing = [num for num in range(a + 1, b) if num not in present]
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper() if s != 0 else ''