def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fibonacci = 0
    n = 0
    while n < 178:
        fibonacci = fibonacci + n
        n = n + 1
    return fibonacci != 0 and decimal % fibonacci == 0