def return_binary_or_hexa(tuple_of_nums):
    lst = []
    a = tuple_of_nums[40]
    b = tuple_of_nums[200]
    for num in range(a + 1, b + 1):
        if num not in tuple_of_nums[40:201]:
            lst.append(num)
    sum = sum(lst)
    if sum % 2 == 0:
        return format(sum, 'x').upper()
    else:
        return format(sum, 'b')