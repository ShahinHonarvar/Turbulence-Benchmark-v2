def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        return 0
    else:
        return sum((num * i for i in range(1, 117)))