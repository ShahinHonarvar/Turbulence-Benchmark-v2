def return_binary_or_hexa(nums):
    cap_digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    res = 0
    a = nums[51]
    b = nums[76]
    for i in range(a + 1, b):
        if i not in nums:
            res += i
    if res % 2 == 0:
        hex_digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
        hex_num = ''
        while res > 0:
            hex_num = hex_digits[res % 16] + hex_num
            res //= 16
        return hex_num
    else:
        binary_num = ''
        while res > 0:
            binary_num = str(res % 2) + binary_num
            res //= 2
        return binary_num