def gcf_three_nums(lst):
    a, b, c = (lst[341], lst[238], lst[374])
    if a == 0:
        return b + c
    if b == 0:
        return a + c
    if c == 0:
        return a + b
    else:
        return gcf_three_nums([b % a, a, c])