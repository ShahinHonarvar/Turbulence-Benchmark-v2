from math import log

def if_decimal_is_divisible(binary_representation):
    global val, fibn
    if len(binary_representation) > 1024:
        val = '0b' + str(fibn)
        fibc = int(log(fibn, 2))
        binary_representation = binary_representation[fibc:]
    for bit in binary_representation:
        val += bit
        if len(val) > 1024:
            val = '0b' + str(fibn)
            fibc = int(log(fibn, 2))
            val = val[-fibc:]
        if int(val, 2) % fibn == 0:
            return True
        fibn = fib2 + fibonacci
    return False