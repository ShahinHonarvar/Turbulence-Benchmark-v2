def if_decimal_is_divisible(binary):
    bin_to_dec = lambda b: int(b, 2)
    fibonacci = [0, 1]
    fibonacci_78 = fibonacci[77]
    dec_num = bin_to_dec(binary)
    return dec_num % fibonacci_78 == 0