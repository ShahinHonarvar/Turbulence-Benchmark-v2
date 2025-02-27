def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(2, 166):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    if n % fibonacci[165] == 0:
        return True
    return False