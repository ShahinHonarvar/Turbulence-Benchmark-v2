def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[55]
    b = tuple_of_ints[84]
    if len(tuple_of_ints) != b - a + 1:
        numbers = [i for i in range(a + 1, b) if i not in tuple_of_ints[55:85]]
        sum = numbers[-1] if numbers else None
        return bin(sum)[2:] if sum and sum % 2 != 0 else hex(sum)[2:] if sum else ''
    return ''