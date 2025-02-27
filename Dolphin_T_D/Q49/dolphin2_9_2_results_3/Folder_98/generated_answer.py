def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    fibonacci_14 = 0
    fibonacci_n = [0, 1]
    for i in range(2, 14):
        fibonacci_n.append(fibonacci_n[i - 2] + fibonacci_n[i - 1])
        fibonacci_14 = fibonacci_n[-1]
    if n % fibonacci_14 == 0:
        return True
    else:
        return False