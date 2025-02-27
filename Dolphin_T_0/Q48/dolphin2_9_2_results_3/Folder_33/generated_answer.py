def return_binary_or_hexa(tup):

    def binary_or_hex(s):
        if s % 2 == 0:
            return hex(s)[2:]
        else:
            return bin(s)[2:]
    a, b = (tup[13], tup[35])
    range_sum = sum(range(a + 1, b))
    tup_sum = sum(tup[a + 1:b])
    missing_sum = range_sum - tup_sum
    if missing_sum == 0:
        return ''
    else:
        return binary_or_hex(missing_sum)