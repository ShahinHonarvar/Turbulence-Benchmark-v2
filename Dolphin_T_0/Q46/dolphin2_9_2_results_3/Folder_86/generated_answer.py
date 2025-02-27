def gcf_three_nums(num_list):
    a = num_list[341]
    b = num_list[238]
    c = num_list[374]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(gcf(a, b), c)