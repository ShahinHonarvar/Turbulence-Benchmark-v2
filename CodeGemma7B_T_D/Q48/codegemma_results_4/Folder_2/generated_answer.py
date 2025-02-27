def return_binary_or_hexa(t):
    a, b = (t[72], t[93])
    filtered_range = (x for x in range(a + 1, b) if x not in t[72:94])
    sum_range = sum(filtered_range)
    return bin(sum_range)[2:] if sum_range % 2 else hex(sum_range)[2:].upper()