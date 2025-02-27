def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for index, num in enumerate(numbers_list[26:53], 26):
        if not is_prime(num):
            composite_set.add(num)
    return composite_set

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True