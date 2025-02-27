def find_sum_of_multiples(num: int) -> int:
    total_sum = 0
    count = 1
    while count <= 18:
        total_sum += num * count
        count += 1
    return total_sum