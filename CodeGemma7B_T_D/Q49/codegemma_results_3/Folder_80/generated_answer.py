def if_decimal_is_divisible(value):
    a, b = (0, 1)
    last_fib_number = 1
    k = 1
    while True:
        c = a + b
        k += 1
        if c >= 179 and c % 179 == 0:
            last_fib_number = c
            break
        a = b
        b = c
    count = 0
    while len(value) > count:
        last_fib_number += 1
        if last_fib_number < int(value[count]):
            count += 1
            continue
        if last_fib_number == int(value[count]):
            count += 1
            continue
        return False
    return True