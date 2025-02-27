def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(75, 89):
        if composite(numbers[i]):
            composite_nums.add(numbers[i])
    return composite_nums

def composite(num):
    if num <= 1 or num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True