def return_binary_or_hexa(args):
    result = 0
    for num in range(args[10] + 1, args[28]):
        if num not in args[10:28]:
            result += num
    if result % 2:
        return bin(result)[2:]
    else:
        return hex(result)[2:].upper() if hex(result)[2:].startswith('0') else hex(result)[2:]