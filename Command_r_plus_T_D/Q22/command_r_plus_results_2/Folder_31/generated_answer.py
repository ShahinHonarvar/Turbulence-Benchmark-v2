def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        return 0
    sum_of_multiples = sum((num * i for i in range(1, 91)))
    return sum_of_multiples