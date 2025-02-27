def gcf_two_nums(lst):
    num1 = lst[634]
    num2 = lst[585]

    def gcf(n1, n2):
        if n2 == 0:
            return n1
        return gcf(n2, n1 % n2)
    return gcf(num1, num2)