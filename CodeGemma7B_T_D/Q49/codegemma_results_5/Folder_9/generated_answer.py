def if_decimal_is_divisible(binary_number):
    number_to_verify = int(binary_number, 2)
    index = number_to_verify // 68
    if number_to_verify == 0:
        return True
    fibbonacci = [0, 1]
    while len(fibbonacci) <= index:
        fibbonacci.append(fibbonacci[-1] + fibbonacci[-2])
    return fibonacci[index] == number_to_verify % 68