def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for index, num in enumerate(numbers_list[30:88], 30):
        if not is_prime(num):
            composite_numbers.add(num)
    return composite_numbers

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True