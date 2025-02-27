def if_decimal_is_divisible(binary):
    binary_length = len(binary)
    result_decimal = int(binary, 2)
    fib_pointer = 1
    fib_terms = [1, 2]
    count = 2
    while result_decimal >= fib_terms[fib_pointer]:
        fib_terms.append(fib_terms[fib_pointer] + fib_terms[fib_pointer - 1])
        fib_pointer += 1
    return True if fib_terms[fib_pointer] % result_decimal == 0 else False