def find_sum_of_multiples(num: int) -> int:
    total_sum = 0
    for i in range(1, 44):
        total_sum += i * num
    return total_sum