def find_sum_of_multiples(num: int) -> int:
    return sum((num * i for i in range(1, 189)))