def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        return 0
    return num * (445 * (445 + 1) // 2)