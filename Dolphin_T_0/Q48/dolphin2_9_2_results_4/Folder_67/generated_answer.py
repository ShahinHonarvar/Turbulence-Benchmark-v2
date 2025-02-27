def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[67]
    are_all_integers_present = all((num in numbers[45:66] for num in range(a + 1, b)))
    if are_all_integers_present:
        return ''
    else:
        the_sum = sum(filter(lambda x: x not in numbers[45:66], range(a + 1, b)))
        if the_sum % 2 == 0:
            return hex(the_sum)[2:]
        else:
            return bin(the_sum)[2:]