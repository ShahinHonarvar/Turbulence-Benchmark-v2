def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_185th_number = 122001604151218792764445725344382398118123457259212296334731287889529121327556063267109876948272674554468448201
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_185th_number == 0