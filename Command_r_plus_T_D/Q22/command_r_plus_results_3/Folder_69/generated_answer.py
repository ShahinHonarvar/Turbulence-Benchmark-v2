def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        return 0
    total_sum = 0
    for i in range(1, 473):
        total_sum += i * num
    return total_sum