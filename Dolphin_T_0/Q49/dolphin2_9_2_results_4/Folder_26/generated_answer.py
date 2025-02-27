def if_decimal_is_divisible(binary):
    integer = int(binary, 2)
    i = 0
    j = 1
    fibonacci = 0
    while fibonacci < integer:
        k = i + j
        i = j
        j = k
        fibonacci = j
    if fibonacci % 138 == 0:
        return True
    else:
        return False