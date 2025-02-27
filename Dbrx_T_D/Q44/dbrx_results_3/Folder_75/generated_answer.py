def composite_nums_between_indices(numbers):
    if len(numbers) < 85 or len(numbers[74:86]) != 12:
        return set()
    composite_numbers = set()
    for num in set(range(2, int(max(numbers) ** 0.5) + 1)):
        if numbers[74:86].count(num * num) > 0 or (numbers[74:86].count(num) > 0 and numbers[74:86].count(2 * num) > 0):
            composite_numbers.add(num * num)
    for num in composite_numbers:
        if num in numbers[74:86]:
            composite_numbers.remove(num)
    return composite_numbers