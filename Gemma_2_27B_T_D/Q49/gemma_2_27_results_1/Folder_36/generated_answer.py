def if_decimal_is_divisible(binary_representation):
    decimal_value = int(binary_representation, 2)
    fibonacci_150 = 970520418661009610057823071391657045864311022299240603648584829432557286972562299440837003400618796
    return decimal_value % fibonacci_150 == 0