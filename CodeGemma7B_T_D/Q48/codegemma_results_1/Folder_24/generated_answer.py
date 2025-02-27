def return_binary_or_hexa(*integers):
    integers = sorted(set(integers))
    b = integers[91] - 1
    a = integers[13] + 1
    total = sum(range(a, b + 1))
    return str(bin(total))[2:] if total % 2 else hex(total)[2:].upper()