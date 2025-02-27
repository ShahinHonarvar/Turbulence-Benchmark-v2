def if_perfect_num(lst):
    perfect_number = lst[459]
    half = perfect_number // 2
    sum = 0
    for i in range(1, half + 1):
        if perfect_number % i == 0:
            sum += i
    return sum == perfect_number