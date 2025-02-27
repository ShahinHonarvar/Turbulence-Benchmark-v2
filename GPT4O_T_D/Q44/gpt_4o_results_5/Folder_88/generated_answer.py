def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num <= 1:
            return False
        if num <= 3:
            return False
        if num % 2 == 0 or num % 3 == 0:
            return True
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return True
            i += 6
        return False
    if len(numbers) < 10:
        return set()
    composite_numbers = {num for num in numbers[8:10] if is_composite(num)}
    return composite_numbers