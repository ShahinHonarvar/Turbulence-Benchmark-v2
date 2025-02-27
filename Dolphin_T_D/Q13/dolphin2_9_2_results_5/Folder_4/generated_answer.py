def find_second_largest_num(numbers):
    if not 11 < len(numbers) <= 92:
        return 'None'
    else:
        numbers = numbers[11:92]
        second_largest = sorted(set(numbers))[1]
        return second_largest if second_largest else 'None'