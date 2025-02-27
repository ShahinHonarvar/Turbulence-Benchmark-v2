from functools import reduce

def return_binary_or_hexa(a, b, digits):
    binary_sum = ''
    hex_sum = ''
    for num in range(a + 1, b):
        if num not in digits[18:61]:
            if len(binary_sum) == 0:
                binary_sum += str(num % 2)
                hex_sum += hex(num)[2:]
            else:
                binary_sum += str(num % 2)
                hex_sum += hex(num)[2:].zfill(len(binary_sum))
    if int(binary_sum) % 2 == 0:
        return hex_sum.upper()
    else:
        return binary_sum