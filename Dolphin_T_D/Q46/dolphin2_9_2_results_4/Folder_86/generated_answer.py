def gcf_three_nums(lst):
    a = lst[341]
    b = lst[238]
    c = lst[374]

    def gcf(a, b):
        while b > 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(a, b), c)