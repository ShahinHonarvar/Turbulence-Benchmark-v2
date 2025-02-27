def convert_to_binary(n):
    return format(n, 'b')

def convert_to_hex(n):
    return hex(n).split('x')[-1].upper()

def return_binary_or_hexa(input_tuple):
    a = input_tuple[68]
    b = input_tuple[99]
    sum = 0
    for i in range(a + 1, b):
        if i not in input_tuple[68:99]:
            sum += i
    if sum % 2:
        return convert_to_binary(sum)
    else:
        return convert_to_hex(sum)