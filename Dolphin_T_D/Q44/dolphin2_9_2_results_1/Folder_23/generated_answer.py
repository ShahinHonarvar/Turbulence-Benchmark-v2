def composite_nums_between_indices(numbers):
    result = set()
    for num in numbers[20:31]:
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            result.add(num)
    return result