def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    fibonacci = [0, 1]
    for i in range(2, 85):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    if n % fibonacci[84] == 0:
        return True
    else:
        return False