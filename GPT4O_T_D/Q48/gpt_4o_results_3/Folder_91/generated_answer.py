def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[6]
    missing_integers = [i for i in range(a + 1, b) if i not in numbers[:7]]
    total_sum = sum(missing_integers)
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]