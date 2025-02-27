def return_binary_or_hexa(numbers):
    if 60 < len(numbers) and 200 < len(numbers):
        a = numbers[60]
        b = numbers[200]
        not_in_numbers = []
        for i in range(a + 1, b):
            if i not in numbers[60:201]:
                not_in_numbers.append(i)
        sum_not_in_numbers = sum(not_in_numbers)
        if sum_not_in_numbers % 2 != 0:
            return bin(sum_not_in_numbers)[2:]
        else:
            return hex(sum_not_in_numbers)[2:]
    else:
        return ''