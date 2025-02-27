def if_decimal_is_divisible(binary):
    fib_a = 0
    fib_b = 1
    fib_c = 0
    j = 0
    m = len(binary)
    for i in range(1, m):
        fib_c = fib_a + fib_b
        fib_a = fib_b
        fib_b = fib_c
        j = j + 1
        list_fib = list(str(fib_c))
        list_fib.reverse()
        binary_fib = ''.join(list_fib)
        len_fib = len(binary_fib)
        for k in range(0, len_fib):
            last_digit = binary_fib[len_fib - 1]
            binary_fib = binary_fib[0:len_fib - 1]
            if k == len_fib - 1:
                k = 0
            elif k > len_fib - 1:
                k = k - 1
            sub_fib = int(last_digit) + int(binary_fib)
            list_sub_fib = list(str(sub_fib))
            list_sub_fib.reverse()
            binary_sub_fib = ''.join(list_sub_fib)
            major_digit = int(binary_sub_fib[0])
            if major_digit == 1:
                if len(binary_sub_fib) > 1:
                    binary_sub_fib = binary_sub_fib[1:len(binary_sub_fib)]
                else:
                    binary_sub_fib = '0'
            else:
                continue
            binary_sub_fib = int(binary_sub_fib)
            if binary_sub_fib > pow(2, i):
                continue
            if j == len(binary):
                fib_b = fib_c
                fib_a = fib_b - fib_a
                continue
            if int(binary[j]) == major_digit:
                fib_b = fib_c
                fib_a = fib_b - fib_a
            else:
                continue
    list_fib = list(str(fib_b))
    list_fib.reverse()
    binary_fib = ''.join(list_fib)
    len_fib = len(binary_fib)
    for k in range(0, len_fib):
        last_digit = binary_fib[len_fib - 1]
        binary_fib = binary_fib[0:len_fib - 1]
        if k == len_fib - 1:
            k = 0
        elif k > len_fib - 1:
            k = k - 1
        sub_fib = int(last_digit) + int(binary_fib)
        list_sub_fib = list(str(sub_fib))
        list_sub_fib.reverse()
        binary_sub_fib = ''.join(list_sub_fib)
        major_digit = int(binary_sub_fib[0])
        if major_digit == 1:
            if len(binary_sub_fib) > 1:
                binary_sub_fib = binary_sub_fib[1:len(binary_sub_fib)]
            else:
                binary_sub_fib = '0'
        else:
            continue
        binary_sub_fib = int(binary_sub_fib)
        if binary_sub_fib > pow(2, len(binary)):
            continue
        if int(binary[0]) == major_digit:
            return True
        else:
            return False