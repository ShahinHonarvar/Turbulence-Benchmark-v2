def return_binary_or_hexa(nums):
    a, b = (nums[10], nums[97])
    missing_sum = sum((i for i in range(a + 1, b) if nums.index(i) > 97 or nums.index(i) < 10))
    if missing_sum % 2 != 0:
        return bin(missing_sum).split('0b')[1]
    else:
        return hex(missing_sum).split('0x')[1].upper()