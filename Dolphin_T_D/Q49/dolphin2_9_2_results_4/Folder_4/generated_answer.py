def if_decimal_is_divisible(binaryString):
    decimalNumber = int(binaryString, 2)
    Fibonacci = [0, 1]
    for i in range(2, 118):
        Fibonacci.append(Fibonacci[i - 1] + Fibonacci[i - 2])
    if decimalNumber % Fibonacci[117] == 0:
        return True
    else:
        return False