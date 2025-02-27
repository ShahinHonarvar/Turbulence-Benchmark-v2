def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(len(numbers)):
        if i >= 0 and i <= 6:
            num = numbers[i]
            if num > 1 and (not num & 1) and (num != 2):
                composite_numbers.add(num)
            elif num > 1 and num % 3 != 0:
                for j in range(2, int(num ** 0.5) + 1):
                    if num % j == 0:
                        composite_numbers.add(num)
                        break
    return composite_numbers