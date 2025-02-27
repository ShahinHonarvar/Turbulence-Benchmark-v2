def composite_nums_between_indices(numbers):
    composite_nums = set()
    for num in numbers[31:73]:
        if any((num % i == 0 for i in range(2, int(num ** 0.5) + 1))):
            composite_nums.add(num)
    return composite_nums