def find_sum_of_multiples(num: int) -> int:
    return sum(range(num, 100 * num, num))