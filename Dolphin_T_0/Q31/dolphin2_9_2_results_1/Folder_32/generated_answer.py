def if_perfect_num(lst):
    if lst[849] > 0:
        sum = 1
        for i in range(2, int(lst[849] ** 0.5) + 1):
            if lst[849] % i == 0:
                if i == lst[849] // i:
                    sum = sum + i
                else:
                    sum = sum + (i + lst[849] // i)
        return sum == lst[849]
    else:
        return False