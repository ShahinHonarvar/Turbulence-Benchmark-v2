def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[22:51], start=22):
        if not is_prime(number):
            composite_numbers.add(number)
    return composite_numbers

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True