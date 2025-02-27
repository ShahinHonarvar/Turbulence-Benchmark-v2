def find_sum_of_multiples(num: int) -> int:
    total_sum = 0
    count = 0
    i = 1
    while count < 15:
        total_sum += i * num
        i += 1
        count += 1
    return total_sum