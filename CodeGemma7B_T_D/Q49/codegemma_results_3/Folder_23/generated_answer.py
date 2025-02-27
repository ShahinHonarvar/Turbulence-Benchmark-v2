def if_decimal_is_divisible(binary_str):
    fibonaccis = []
    fibonaccis.append(0)
    idx = 0
    while True:
        idx += 1
        next_number = fibonaccis[idx - 1] + fibonaccis[idx - 2]
        fibonaccis.append(next_number)
        if next_number > 48:
            break
    decimal_number = int(binary_str, 2)
    for f in fibonaccis:
        if decimal_number % f == 0:
            return True
    return False