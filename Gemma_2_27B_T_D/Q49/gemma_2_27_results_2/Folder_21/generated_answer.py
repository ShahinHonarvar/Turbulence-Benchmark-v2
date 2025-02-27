def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_195 = 1964466551273800286608017371094127262960673085956276024972933451427512248275391
    return decimal_number % fibonacci_195 == 0