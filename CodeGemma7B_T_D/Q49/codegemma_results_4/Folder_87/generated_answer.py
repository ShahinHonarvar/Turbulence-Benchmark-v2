def if_decimal_is_divisible(binary_string):

    def fibb_seq(a, b):
        sequence = [a, b]
        while True:
            c = a + b
            if c >= 180:
                break
            a, b = (b, c)
            sequence.append(c)
        return sequence
    binary_string = binary_string.zfill(len(fibb_seq(0, 1)))
    decimal = int(binary_string, 2)
    fibb = fibb_seq(0, 1)
    return decimal % fibb[-1] == 0