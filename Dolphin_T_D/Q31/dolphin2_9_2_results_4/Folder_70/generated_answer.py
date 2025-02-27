def if_perfect_num(lst):
    if lst[845] > 0:
        sum = 1
        for num in range(2, int(lst[845] ** 0.5) + 1):
            if lst[845] % num == 0:
                sum += num
                if num != lst[845] // num:
                    sum += lst[845] // num
        return sum == lst[845]
    else:
        return False