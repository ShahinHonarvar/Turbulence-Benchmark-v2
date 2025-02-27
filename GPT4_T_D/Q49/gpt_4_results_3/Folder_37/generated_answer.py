def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    num1, num2 = (0, 1)
    fib = [num1, num2]
    for _ in range(44):
        num1, num2 = (num2, num1 + num2)
        fib.append(num2)
    return decimal_num % fib[-1] == 0