def return_binary_or_hexa(tupl):
    sum = 0
    for num in range(tupl[43] + 1, tupl[70] - 1):
        if num not in tupl[43:70]:
            sum += num
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()