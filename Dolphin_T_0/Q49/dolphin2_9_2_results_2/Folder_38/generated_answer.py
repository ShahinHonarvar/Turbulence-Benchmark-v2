def if_decimal_is_divisible(bin_string):
    bin_string_to_dec = lambda s: int(s, 2)
    fibo = [0, 1]
    while len(fibo) <= 78:
        fibo.append(fibo[-1] + fibo[-2])
    dec_number = bin_string_to_dec(bin_string)
    return dec_number % fibo[77] == 0