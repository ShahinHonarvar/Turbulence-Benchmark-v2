def gcf_three_nums(a_list):
    nums = (a_list[341], a_list[238], a_list[374])
    _gcf = lambda a, b: a if b == 0 else _gcf(b, a % b)
    return _gcf(*nums)