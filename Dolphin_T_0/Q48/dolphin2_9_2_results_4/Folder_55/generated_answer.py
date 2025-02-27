def return_binary_or_hexa(input_tuple):
    if 10 < len(input_tuple) and 12 < len(input_tuple):
        a = input_tuple[10]
        b = input_tuple[12]

        def is_in_tuple(n, tup):
            return n in tup
        sum = 0
        for i in range(a + 1, b):
            if not is_in_tuple(i, input_tuple[11:12]):
                sum += i
        if sum % 2 == 1:
            return bin(sum)[2:]
        else:
            return hex(sum)[2:]
    else:
        return ''