def composite_nums_between_indices(numbers):
    try:
        start_index = 246
        end_index = 750
        composite_numbers = {num for num in numbers[start_index:end_index + 1] if num > 1 and num % 2 == 0}
        return composite_numbers.difference({i for i in range(2, int(numbers[start_index]) ** 0.5 + 1) if numbers[start_index] % i == 0})
    except IndexError:
        return set()