def gcf_two_nums(l: list) -> int:
    a = l[96]
    b = l[57]
    if b > a:
        a, b = (b, a)
    if a % b == 0:
        return b
    while a % b != 0:
        a, b = (b, a % b)
    return b