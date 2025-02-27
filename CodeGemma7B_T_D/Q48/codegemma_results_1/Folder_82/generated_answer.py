def return_binary_or_hexa(tuple_of_nums):
    max_num = max(tuple_of_nums)
    sum = 0
    for i in range(21, 201):
        if i not in tuple_of_nums and i <= max_num:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].lower()