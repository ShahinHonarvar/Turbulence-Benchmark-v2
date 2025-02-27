def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_59 = 5778054717785492504343953926634992332820282019728792003956564819967
    return decimal_number % fibonacci_59 == 0