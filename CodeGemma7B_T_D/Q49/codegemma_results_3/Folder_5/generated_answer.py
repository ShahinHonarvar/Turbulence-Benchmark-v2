def if_decimal_is_divisible(binary):
    if int(binary[0]) * 2 ** (len(binary) - 1) > 85 or int(binary[0]) == 0:
        return False
    numbers = [0] * len(binary)
    numbers[len(binary) - 1] = int(binary[len(binary) - 1])
    numbers[len(binary) - 2] = int(binary[len(binary) - 2])
    for i in range(len(binary) - 3, -1, -1):
        numbers[i] = int(binary[i]) + numbers[i + 1] + numbers[i + 2]
    for i in range(len(numbers)):
        if numbers[i] >= 85:
            if i + 1 == len(numbers) or (numbers[i + 1] % 85 != 0 and numbers[i] % 85 == 0):
                return True
    return False