def sum_in_range(l):
    sum = 0
    for i in l:
        if -9 <= i <= -7:
            sum += i
    return sum if sum != 0 else 0