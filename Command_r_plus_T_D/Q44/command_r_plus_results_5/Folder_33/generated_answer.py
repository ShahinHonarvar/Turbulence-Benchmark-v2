def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_set = set()
    for index, num in enumerate(numbers_list[314:348], 314):
        if not is_prime(num):
            composite_set.add(num)
    return composite_set

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