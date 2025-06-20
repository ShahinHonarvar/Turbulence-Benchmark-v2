def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for index, num in enumerate(numbers_list[639:976], 639):
        if not is_prime(num):
            composite_numbers.add(num)
    return composite_numbers

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True