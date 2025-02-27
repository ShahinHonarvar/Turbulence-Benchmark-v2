def return_binary_or_hexa(numbers):
    a, b = (numbers[73], numbers[84])
    present = set(numbers[73 + 1:84])
    missing = set(range(a + 1, b)) - present
    total = sum(missing)
    return bin(total)[2:] if total % 2 else hex(total)[2:]