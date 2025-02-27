def find_sum_of_multiples(num: int) -> int:
    result = 0
    for i in range(1, 97):
        result += i * num
    return result