def if_decimal_is_divisible(binary_representation):
    fib, count, result, alpha = (0, 2, 0, 0)
    while len(binary_representation) > 1:
        if fib <= int(binary_representation[-1], 2):
            result += int(binary_representation[-1], 2) * 2 ** count
            alpha += 1
        elif alpha == 1:
            count += 1
            fib = fib ** 2
            fib += 2 ** count
            if fib > int(binary_representation, 2):
                fib -= 2 ** count
            continue
        else:
            alpha = 0
            fib = fib ** 2
            fib += 2 ** count
            if fib > int(binary_representation, 2):
                fib -= 2 ** count
            count += 1
    if fib <= int(binary_representation[-1], 2):
        result += int(binary_representation[-1], 2) * 2 ** count
    elif alpha == 1:
        count += 1
        fib = fib ** 2
        fib += 2 ** count
        if fib > int(binary_representation, 2):
            fib -= 2 ** count
        result += fib // 10
    else:
        result += fib // 10
    if result % 286 == 0:
        return True
    else:
        return False