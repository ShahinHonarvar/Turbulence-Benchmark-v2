def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_176th_number = 1954960345163931779126152314209320369914791700819750005311107977868405777019242969020001
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_176th_number == 0