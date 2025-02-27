def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_84th_number = 1386492126608598352404331283220473085319531324229759605440850512121029228649671858407713874578
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_84th_number == 0