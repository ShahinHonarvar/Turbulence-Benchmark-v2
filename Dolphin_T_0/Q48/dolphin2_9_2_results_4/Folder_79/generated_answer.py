def return_binary_or_hexa(inputs):
    a, b = (inputs[1], inputs[7])
    all_numbers = set(range(a + 1, b))
    our_numbers = set(inputs[1:8])
    missing_numbers = all_numbers.difference(our_numbers)
    total_sum = sum(missing_numbers)
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()