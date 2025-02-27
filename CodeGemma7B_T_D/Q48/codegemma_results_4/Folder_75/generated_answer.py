def return_binary_or_hexa(nums):
    sum = 0
    for num in range(21, 52):
        if num not in nums:
            sum += num
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()