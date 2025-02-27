def if_perfect_num(lst):
    if lst[321] > 0:
        sum = 1
        for i in range(2, int(lst[321] ** 0.5) + 1):
            if lst[321] % i == 0:
                if i == lst[321] // i:
                    sum += i
                else:
                    sum += i + lst[321] // i
        return sum == lst[321]
    return False