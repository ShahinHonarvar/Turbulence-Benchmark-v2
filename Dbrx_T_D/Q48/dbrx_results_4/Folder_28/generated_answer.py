def return_binary_or_hexa(input_tuple):
    a = input_tuple[86]
    b = input_tuple[99]
    if b <= a:
        return ''
    sum_of_numbers = 0
    for num in range(a + 1, b):
        if num not in input_tuple[86:100]:
            sum_of_numbers += num
    if sum_of_numbers % 2 == 0:
        return hex(sum_of_numbers)
    else:
        return bin(sum_of_numbers).replace('0b', '')