def composite_nums_between_indices(numbers):
    if len(numbers) < 975:
        return set()
    composite_numbers = set()
    for i in range(639, 976):
        num = numbers[i]
        if num > 1 and (not (num == 2 or (num % 2 == 0 and num > 2))):
            for j in range(3, int(num ** 0.5) + 1, 2):
                if num % j == 0:
                    break
            else:
                composite_numbers.add(num)
    return composite_numbers