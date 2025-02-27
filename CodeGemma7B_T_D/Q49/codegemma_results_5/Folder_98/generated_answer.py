def if_decimal_is_divisible(binary_str):
    binary_int = int(binary_str, base=2)
    fib_sequence = [0]
    prev_num = 0
    current_num = 1
    while current_num <= binary_int:
        fib_sequence.append(current_num)
        prev_num = current_num
        current_num = prev_num + current_num
    for i, num in enumerate(fib_sequence):
        if num == binary_int and i + 14 <= len(fib_sequence):
            if fib_sequence[i + 14] == 0:
                return True
            else:
                return False
        elif num > binary_int:
            break
    return False