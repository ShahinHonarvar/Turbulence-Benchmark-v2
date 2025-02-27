def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[77], numbers[84])
    sum_values = sum(range(a + 1, b))
    missing_values = [i for i in range(a + 1, b) if i not in numbers[78:84]]
    sum_missing = sum(missing_values)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]