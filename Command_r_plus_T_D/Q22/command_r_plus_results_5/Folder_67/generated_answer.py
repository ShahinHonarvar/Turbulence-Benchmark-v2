def find_sum_of_multiples(num: int) -> int:
    sum_of_multiples = 0
    for i in range(1, 43):
        sum_of_multiples += i * num
    return sum_of_multiples