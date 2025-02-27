def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        return 0
    sum_of_multiples = 0
    for i in range(1, 57):
        sum_of_multiples += i * num
    return sum_of_multiples