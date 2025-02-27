def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_198th_num = 9463858022324945299473507051506379244814277189997679203483475405042088383973676115472015
    binary_int = int(binary_str, 2)
    return binary_int % fib_198th_num == 0