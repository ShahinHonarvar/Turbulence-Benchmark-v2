def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[70], numbers[200])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in numbers[70:201]:
            sum_ += i
    if sum_ == 0:
        return ''
    return sum_.to_bytes((sum_.bit_length() + 7) // 8, 'big').hex().upper() if sum_ % 2 == 0 else bin(sum_)[2:]