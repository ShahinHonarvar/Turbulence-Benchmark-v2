def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    sum_ = 0
    range_ = numbers[81:87]
    for i in range(numbers[81] + 1, numbers[86]):
        if i not in range_:
            sum_ += i
    if sum_ == 0:
        return ''
    return sum_.to_bytes((sum_.bit_length() + 7) // 8, 'big').hex().upper() if sum_ % 2 == 0 else bin(sum_)[2:]