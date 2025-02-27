def gcf_three_nums(lst):
    a = lst[78]
    b = lst[19]
    c = lst[13]
    gcf_abc = a
    while b != 0 and c != 0:
        gcf_abc = b = c = 0
        temp = min(a, b, c)
        while temp != 0:
            if a % temp == 0 and b % temp == 0 and (c % temp == 0):
                gcf_abc = temp
            else:
                a = a - temp
                b = b - temp
                c = c - temp
            if a == b and b == c and (c == 0):
                break
            temp = min(a, b, c)
    return gcf_abc