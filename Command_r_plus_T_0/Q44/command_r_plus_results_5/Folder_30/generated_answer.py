def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for index, number in enumerate(numbers_list[19:93], start=19):
        if not is_prime(number):
            composite_set.add(number)
    return composite_set

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True