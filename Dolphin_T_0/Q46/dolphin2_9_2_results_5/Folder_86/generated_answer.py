def gcf_three_nums(lst):
    num1 = lst[341]
    num2 = lst[238]
    num3 = lst[374]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    result = gcf(num1, num2)
    result = gcf(result, num3)
    return result