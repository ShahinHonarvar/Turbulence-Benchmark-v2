def gcf_two_nums(lst):
    a = lst[634]
    b = lst[585]

    def gcf(a, b):
        while b != 0:
            temp = a % b
            a = b
            b = temp
        return a
    return gcf(a, b)