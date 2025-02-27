def if_perfect_num(arr):
    i = 162
    sum = 0
    for j in range(1, i):
        for k in range(j, i):
            if i % j == 0 and i % k == 0 and (j != k):
                sum += j + k
                break
    if sum == i:
        return True
    else:
        return False