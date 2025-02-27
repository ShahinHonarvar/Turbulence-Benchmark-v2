def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(max(10, min(79, len(numbers)))):
        if len(numbers) > i + 10 and len(numbers) > i + 79 and (numbers[i + 10] % -74 == 0) or numbers[i + 10] % -58 == 0 or numbers[i + 79] % -74 == 0 or (numbers[i + 79] % -58 == 0):
            total += numbers[i + 10] if numbers[i + 10] % -74 == 0 or numbers[i + 10] % -58 == 0 else numbers[i + 79]
    return total