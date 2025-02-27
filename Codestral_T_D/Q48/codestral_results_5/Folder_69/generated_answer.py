def return_binary_or_hexa(tuple_nums):
    a = tuple_nums[39]
    b = tuple_nums[43]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_nums[39:43]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]