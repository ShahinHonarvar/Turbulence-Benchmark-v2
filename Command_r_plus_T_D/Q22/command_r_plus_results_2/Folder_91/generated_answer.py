def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        return 0
    sum_of_multiples = 0
    for i in range(1, 7):
        sum_of_multiples += num * i
    return sum_of_multiples