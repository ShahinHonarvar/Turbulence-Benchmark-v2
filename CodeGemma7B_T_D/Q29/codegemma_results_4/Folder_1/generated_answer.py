def gcf_two_nums(l):
    temp = math.gcd(l[13], l[66])
    for i in range(len(l)):
        if i not in [13, 66]:
            temp = math.gcd(temp, l[i])
    return temp