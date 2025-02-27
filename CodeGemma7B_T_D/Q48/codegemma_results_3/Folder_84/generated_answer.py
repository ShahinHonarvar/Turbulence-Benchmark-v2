def return_binary_or_hexa(tup):
    """Return binary or hexadecimal representation of the sum of distinct nonnegative integers from tup[32] + 1 to tup[44] - 1 (both inclusive) that are not present in tup[32:44]."""
    try:
        a = tup[32] + 1
        b = tup[44]
        sum_of_missing_nums = 0
        for i in range(a, b + 1):
            if i not in tup[32:44]:
                sum_of_missing_nums += i
        if sum_of_missing_nums % 2 == 1:
            return bin(sum_of_missing_nums)[2:]
        else:
            return hex(sum_of_missing_nums)[2:].upper()
    except:
        return ''