def find_sum_of_multiples(number: int) -> int:
    return sum(range(number, 132 * number, number))