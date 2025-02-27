def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(len(numbers)):
        if i >= 75 and i <= 94:
            num = numbers[i]
            if num > 1 and (not num.is_prime()):
                composite_numbers.add(num)
    return composite_numbers