def return_binary_or_hexa(numbers):
    if 57 <= 85 < len(numbers):
        a = numbers[57]
        b = numbers[85]
        present_numbers = set(range(a + 1, b))
        missing_numbers = [i for i in present_numbers if i not in numbers]
        sum_missing_numbers = 0
        for number in missing_numbers:
            sum_missing_numbers += number
        if sum_missing_numbers % 2 == 0:
            return hex(sum_missing_numbers)[2:]
        else:
            return bin(sum_missing_numbers)[2:]
    else:
        return ''