def if_perfect_num(lst):
    perfect_sum = 1
    if len(lst) < 43:
        return False
    number = lst[42]
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            perfect_sum += i
            if i != number // i:
                perfect_sum += number // i
    return perfect_sum == number and perfect_sum > 1