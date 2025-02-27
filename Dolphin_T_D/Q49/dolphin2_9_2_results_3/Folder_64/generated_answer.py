def if_decimal_is_divisible(binaryString):
    decimalPlace = 0
    binaryString = str(binaryString)
    decimal = 0
    for i in range(len(binaryString)):
        decimal += int(binaryString[len(binaryString) - i - 1]) * pow(2, decimalPlace)
        decimalPlace += 1
    num1 = 0
    num2 = 1
    currentNum = 0
    i = 0
    while i < 10:
        if currentNum == 0:
            currentNum = num1 + num2
            num1 = num2
            num2 = currentNum
        else:
            currentNum = num2 + num1
            num1 = num2
            num2 = currentNum
        i += 1
    if decimal % currentNum == 0:
        return True
    else:
        return False