def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        return 0
    else:
        return num * (472 * (472 + 1)) // 2