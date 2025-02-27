def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_177th = 19075580428263935506709048204945108689217853717953821491873511532248797346950302
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_177th == 0