def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    range_start = numbers[69] + 1
    range_end = numbers[97] - 1
    range_sum = 0
    for num in range(range_start, range_end + 1):
        if num not in numbers[69:98]:
            range_sum += num
    if range_sum:
        return bin(range_sum)[2:] if range_sum % 2 else hex(range_sum)[2:].upper()
    else:
        return ''