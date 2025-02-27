def return_binary_or_hexa(tuple_of_nums):
    a = tuple_of_nums[44]
    b = tuple_of_nums[67]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_of_nums[44:67]:
            sum += i
    if sum % 2 == 1:
        return str(bin(sum))[2:]
    else:
        return hex(sum)[2:].upper()