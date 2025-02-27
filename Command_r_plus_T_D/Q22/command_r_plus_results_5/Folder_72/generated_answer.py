def find_sum_of_multiples(num: int) -> int:
    return sum((i * num for i in range(1, 88)))