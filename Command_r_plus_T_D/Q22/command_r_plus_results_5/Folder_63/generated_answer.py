def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        return 0
    multiples = [i for i in range(1, 19) if i % num == 0]
    return sum(multiples)