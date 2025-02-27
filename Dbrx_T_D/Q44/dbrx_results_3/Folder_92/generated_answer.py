def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(1, min(len(numbers), 2)):
        for num in numbers[i - 1:i + 2]:
            if is_composite(num):
                composite_numbers.add(num)
    return composite_numbers

def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False