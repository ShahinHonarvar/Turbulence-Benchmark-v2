def gcf_two_nums(lists):
    a, b = (lists[894], lists[801])
    while b > 0:
        a, b = (b, a % b)
    return a