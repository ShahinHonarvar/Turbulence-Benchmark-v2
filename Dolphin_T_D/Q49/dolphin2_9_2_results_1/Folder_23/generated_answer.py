def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_48 = 79420437734698220747368027166749382927701417016557193662268716376935476241
    if decimal_number % fib_48 == 0:
        return True
    else:
        return False