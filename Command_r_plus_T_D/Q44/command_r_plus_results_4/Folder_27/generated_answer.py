def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_nums = set()
    for index, num in enumerate(numbers_list[22:64], start=22):
        if not is_prime(num):
            composite_nums.add(num)
    return composite_nums

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True