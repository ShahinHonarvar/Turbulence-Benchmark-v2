def return_binary_or_hexa(t):
    desired_sum = sum((n for n in range(t[10] + 1, t[100] - 1) if n not in t[10:100]))
    return bin(desired_sum)[2:] if desired_sum % 2 else hex(desired_sum)[2:].upper()