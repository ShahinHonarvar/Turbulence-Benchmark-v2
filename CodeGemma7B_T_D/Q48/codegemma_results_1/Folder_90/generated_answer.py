def return_binary_or_hexa(integers):
    assert len(integers) == 130, 'Invalid tuple length'
    a, b = (integers[60], integers[90])
    sum_of_missing_integers = 0
    for i in range(a + 1, b):
        if i not in integers[60:91]:
            sum_of_missing_integers += i
    if sum_of_missing_integers % 2 == 1:
        return f'{sum_of_missing_integers:b}'
    else:
        return f'{sum_of_missing_integers:x}'