def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[34:56], start=34):
        if not is_prime(number):
            composite_numbers.add(number)
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