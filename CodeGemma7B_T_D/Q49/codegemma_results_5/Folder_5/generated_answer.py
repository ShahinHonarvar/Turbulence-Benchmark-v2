def if_decimal_is_divisible(bit_string):
    fibbo = [0, 1]
    for i in range(2, 85):
        fibbo.append(fibbo[i - 2] + fibbo[i - 1])
    fibbo_85th = fibbo[84]
    decimal_number = 0
    for i in range(len(bit_string)):
        if bit_string[-i - 1] == '1':
            decimal_number += 2 ** i
    if decimal_number % fibbo_85th == 0:
        return True
    else:
        return False