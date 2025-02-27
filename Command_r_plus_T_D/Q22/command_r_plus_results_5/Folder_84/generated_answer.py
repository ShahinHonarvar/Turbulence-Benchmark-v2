def find_sum_of_multiples(number: int) -> int:
    sum_of_multiples = 0
    for i in range(1, 132):
        sum_of_multiples += number * i
    return sum_of_multiples