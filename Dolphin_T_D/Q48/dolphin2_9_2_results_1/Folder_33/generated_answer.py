def return_binary_or_hexa(t):
    a, b = (t[13], t[35])
    missing_numbers = [x for x in range(a + 1, b) if x not in t]
    if len(missing_numbers) == 0:
        return ''
    else:
        sum_ = sum(missing_numbers)
        if sum_ % 2 == 0:
            return hex(sum_)[2:].upper()
        else:
            return bin(sum_)[2:]