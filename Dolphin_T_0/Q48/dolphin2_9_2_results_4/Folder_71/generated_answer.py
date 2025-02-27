def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[20]
    b = tuple_of_integers[35]
    if a + 1 > b - 1:
        return ''
    sum_in_range = sum(range(a + 1, b))
    for num in tuple_of_integers[20:36]:
        if num >= a + 1 and num < b:
            sum_in_range -= num
    if sum_in_range % 2 == 0:
        return hex(sum_in_range)[2:]
    else:
        return bin(sum_in_range)[2:]