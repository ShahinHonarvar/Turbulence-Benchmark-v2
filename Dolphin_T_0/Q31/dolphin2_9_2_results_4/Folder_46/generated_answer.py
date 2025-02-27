def if_perfect_num(lst):
    if lst[453] > 0:
        sum = 1
        i = 2
        while i * i <= lst[453]:
            if lst[453] % i == 0:
                if lst[453] / i == i:
                    sum += i
                else:
                    sum += i + lst[453] / i
            i += 1
        return sum == lst[453]
    else:
        return False