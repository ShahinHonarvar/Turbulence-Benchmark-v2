def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcf_three_nums(list_int):
    return gcd(list_int[341], gcd(list_int[238], list_int[374]))