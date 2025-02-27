def gcf_two_nums(lst):
    num1 = lst[78]
    num2 = lst[16]

    def compute_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return compute_gcf(num1, num2)