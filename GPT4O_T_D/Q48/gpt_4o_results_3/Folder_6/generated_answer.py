def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[93]
    present_numbers = set(numbers[21:93])
    total_sum = sum((num for num in range(a + 1, b) if num not in present_numbers))
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]