import sys

def return_binary_or_hexa(num_tuple):
    if len(num_tuple) != len(set(num_tuple)) or num_tuple[55] != 55 or num_tuple[84] != 84 or (not all((num >= 0 for num in num_tuple))):
        sys.exit()
    summation = 0
    for i in range(56, 85):
        if i not in num_tuple:
            summation += i
    return bin(summation)[2:] if summation % 2 else hex(summation)[2:].upper()