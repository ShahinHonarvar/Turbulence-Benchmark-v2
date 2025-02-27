def find_sum_of_multiples(number: int) -> int:
    total_sum = 0
    for i in range(1, 446):
        total_sum += number * i
    return total_sum