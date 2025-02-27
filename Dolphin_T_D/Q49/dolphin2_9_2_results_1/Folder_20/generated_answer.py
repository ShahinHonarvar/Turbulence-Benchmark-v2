def if_decimal_is_divisible(binary):
    i = 0
    fibonacci = [0, 1]
    while len(binary) > i:
        if i <= 1:
            fib_number = fibonacci[i]
        else:
            fib_number = fibonacci[i - 1] + fibonacci[i - 2]
            if fib_number > 100:
                fibonacci.append(fib_number)
                return binary % fib_number == 0
            else:
                fibonacci.append(fib_number)
        i += 1
    return False