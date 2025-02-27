def gcf_three_nums(num_list):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    a = num_list[341]
    b = num_list[238]
    c = num_list[374]
    return gcf(gcf(a, b), c)