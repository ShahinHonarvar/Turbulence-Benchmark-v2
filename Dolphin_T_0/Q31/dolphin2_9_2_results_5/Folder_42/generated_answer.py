def if_perfect_num(lst):
    if lst[276] > 0:
        sum = 1
        for i in range(1, int(lst[276] ** 0.5) + 1):
            if lst[276] % i == 0:
                if i != lst[276] // i:
                    sum = sum + i + lst[276] // i
                else:
                    sum = sum + i
        return sum == lst[276]
    else:
        return False