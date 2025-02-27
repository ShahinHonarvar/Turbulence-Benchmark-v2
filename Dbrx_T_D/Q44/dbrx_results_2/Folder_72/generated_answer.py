def composite_nums_between_indices(numbers):
    composite_set = set()
    for i in range(len(numbers)):
        if i >= 55 and i <= 98:
            num = numbers[i]
            if num > 1 and (not num.is_prime()):
                composite_set.add(num)
    return composite_set