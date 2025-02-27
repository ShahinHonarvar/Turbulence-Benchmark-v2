def find_sum_of_multiples(num: int) -> int:
    return sum(range(num, 132 * num, num))