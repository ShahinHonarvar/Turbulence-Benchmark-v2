def find_sum_of_multiples(num: int) -> int:
    sum_of_multiples = sum((num * i for i in range(1, 20)))
    return sum_of_multiples