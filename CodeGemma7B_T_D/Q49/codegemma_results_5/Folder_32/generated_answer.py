def if_decimal_is_divisible(binary):
    l = [0] * (len(binary) + 1)
    l[0], l[1] = (0, 1)
    for i in range(2, len(l)):
        l[i] = l[i - 1] + l[i - 2]
    x = int(binary, 2)
    while x >= l[-1]:
        l.append(l[-2] + l[-1])
    if x in {i for i in l if i % 178 == 0}:
        return True
    return False