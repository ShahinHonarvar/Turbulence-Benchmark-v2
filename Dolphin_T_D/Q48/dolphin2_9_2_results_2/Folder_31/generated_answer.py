def return_binary_or_hexa(nums_tuple):
    a = nums_tuple[33]
    b = nums_tuple[78]
    sum = 0
    for num in range(a + 1, b):
        if num not in nums_tuple[33:79]:
            sum += num
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]