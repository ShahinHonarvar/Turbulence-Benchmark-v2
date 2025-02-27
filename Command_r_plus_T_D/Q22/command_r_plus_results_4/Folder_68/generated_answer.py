def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        return 0
    else:
        return num * 4 * (4 + 1) // 2