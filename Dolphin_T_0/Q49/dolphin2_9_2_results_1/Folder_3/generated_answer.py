def if_decimal_is_divisible(binary_decimal):
    decVal = int(binary_decimal, 2)
    fib35 = 101407932194664399081
    return decVal % fib35 == 0