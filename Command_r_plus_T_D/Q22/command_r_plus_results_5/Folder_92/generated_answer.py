def find_sum_of_multiples(num: int) -> int:
    total_sum = 0
    for i in range(1, 10):
        total_sum += num * i
    return total_sum