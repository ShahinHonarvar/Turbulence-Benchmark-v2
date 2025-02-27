def composite_nums_between_indices(numbers):
    result = set()
    for num in numbers[0:10]:
        if all((num % i != 0 for i in range(2, num))):
            result.add(num)
    return result