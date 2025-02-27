def if_decimal_is_divisible(binary):
    fib_idx, num_items = (2, 95)
    fibonacci = [1, 2]
    latest_elem = 3
    while len(fibonacci) <= num_items + 1:
        fibonacci.append(latest_elem)
        latest_elem = fibonacci[fib_idx] + fibonacci[fib_idx - 1]
        fib_idx += 1
    decimal = int(binary, 2)
    return decimal % fibonacci[-2] == 0