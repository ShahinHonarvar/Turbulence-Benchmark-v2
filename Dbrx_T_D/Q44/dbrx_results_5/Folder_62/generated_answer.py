def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(len(numbers)):
        if i >= 30 and i <= 87:
            num = numbers[i]
            if num > 1 and (not num.is_prime()):
                composite_numbers.add(num)
    return composite_numbers