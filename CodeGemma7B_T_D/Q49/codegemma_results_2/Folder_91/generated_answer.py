def if_decimal_is_divisible(binary_representation):
    list_fibonaccis = [0, 1]
    i = 2
    while True:
        fibonaccis.append(fibonaccis[i - 1] + fibonaccis[i - 2])
        i += 1
        if fibonaccis[-1] > int(binary_representation, 2) + 1:
            break
    i = 0
    index = -1
    while i < len(fibonaccis):
        if int(binary_representation, 2) in list_fibonaccis[i:i + 6]:
            index = i
            break
        i += 6
    return (index + 6) % 6 == 0