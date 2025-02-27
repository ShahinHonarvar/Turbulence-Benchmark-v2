def if_perfect_num(lst):
    if len(lst) < 686:
        return False
    number = lst[685]
    perfect_sum = sum((i for i in range(1, number) if number % i == 0))
    return perfect_sum == number