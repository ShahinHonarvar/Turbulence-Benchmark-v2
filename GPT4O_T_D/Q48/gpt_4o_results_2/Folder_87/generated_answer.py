def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[43]
    nums_between_a_and_b = numbers[20:44]
    total_sum = sum((n for n in range(a + 1, b) if n not in nums_between_a_and_b))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]