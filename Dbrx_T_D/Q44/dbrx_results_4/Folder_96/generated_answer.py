def composite_nums_between_indices(numbers):
    composite_nums = {i for i in range(4, 257) if i % 2 != 0 and i % 3 != 0 or (i % 2 == 0 and i > 4)}
    result = numbers[60:201]
    return set(result) & composite_nums