def if_decimal_is_divisible(binary_rep):
    max_length = int(len(binary_rep) / 2)
    binary_reps = [binary_rep[i:i + max_length] for i in range(0, len(binary_rep), max_length)]
    binarys = [int(i, 2) for i in binary_reps]
    fibs = [0, 1]
    for num in range(2, 64):
        fibs.append(fibs[num - 1] + fibs[num - 2])
    index = 0
    while index < len(binarys):
        if binarys[index] in fibs[:78]:
            if (index + 1) % 3 == 0:
                return True
        index += 1
    return False