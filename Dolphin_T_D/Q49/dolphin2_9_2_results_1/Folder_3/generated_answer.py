def if_decimal_is_divisible(bin_num):
    dec_num = int(bin_num, 2)
    fibonacci = [0, 1]
    for i in range(2, 36):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    thirty_fifth_fibonacci = fibonacci[34]
    return dec_num % thirty_fifth_fibonacci == 0