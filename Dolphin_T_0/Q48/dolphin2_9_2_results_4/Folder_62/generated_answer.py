def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[91]
    present_numbers = set(range(a + 1, b))
    for number in numbers[50:92]:
        if number in present_numbers:
            present_numbers.remove(number)
    if not present_numbers:
        return ''
    sum_of_numbers = sum(present_numbers)
    if sum_of_numbers % 2 == 1:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:]