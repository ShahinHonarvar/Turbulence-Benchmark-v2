def if_perfect_num(lst):
    if lst[87] < 1:
        return False
    else:
        sum = 1
        i = 2
        while i * i <= lst[87]:
            if lst[87] % i:
                i += 1
            else:
                if i * (lst[87] // i) == lst[87]:
                    sum = sum + i + lst[87] // i
                else:
                    sum = sum + i
                i += 1
        return sum == lst[87]