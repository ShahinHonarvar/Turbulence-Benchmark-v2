def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_118th_number = 192936912556919304750997172472037442396454873930138749482143362277744110346624082023716179294135899447517419289890502563
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_118th_number == 0