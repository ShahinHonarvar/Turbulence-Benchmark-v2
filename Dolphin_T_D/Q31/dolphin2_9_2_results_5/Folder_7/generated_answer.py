def if_perfect_num(lst):
    if lst[851] > 0:
        sum_divs = 1
        i = 2
        while i * i <= lst[851]:
            if lst[851] % i:
                i += 1
            elif lst[851] // i == i:
                sum_divs = sum_divs + i
            else:
                sum_divs = sum_divs + (i + lst[851] // i)
            i += 1
        return sum_divs == lst[851]
    else:
        return False