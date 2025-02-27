def find_sum_of_multiples(number: int) -> int:
    return sum((number * i for i in range(1, 446)))