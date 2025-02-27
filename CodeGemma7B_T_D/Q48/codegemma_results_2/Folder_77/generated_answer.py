def return_binary_or_hexa(nums):
    sum = 0
    for i in range(19, 53):
        if i not in nums:
            sum += i
    if sum % 2:
        res = str(bin(sum))[2:]
    else:
        res = hex(sum)[2:].upper()
    return res