def if_decimal_is_divisible(binary_string):
    fibbonaci_sequence = {'0': 0, '1': 1}
    for i in range(2, 137):
        fibbonaci_sequence['0' + str(i)] = sum((fibbonaci_sequence['0' + str(j)] for j in range(i - 1, max(0, i - 47), -1)))
        fibbonaci_sequence['1' + str(i)] = sum((fibbonaci_sequence['1' + str(j)] for j in range(i - 1, max(0, i - 47), -1))) + fibbonaci_sequence['0' + str(i)]
    return binary_string in fibbonaci_sequence.keys()