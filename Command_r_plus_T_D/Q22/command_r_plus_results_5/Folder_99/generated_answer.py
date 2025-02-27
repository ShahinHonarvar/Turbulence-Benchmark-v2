def find_sum_of_multiples(num: int) -> int:
    return sum(range(0, 421 * num, num))