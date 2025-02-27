def find_sum_of_multiples(multiple: int) -> int:
    return sum((multiple * i for i in range(1, 25)))