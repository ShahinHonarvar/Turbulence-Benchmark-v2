def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_105th_number = 1370802469608750524626404027034187908714881006040046183562109910292383327390400500
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_105th_number == 0