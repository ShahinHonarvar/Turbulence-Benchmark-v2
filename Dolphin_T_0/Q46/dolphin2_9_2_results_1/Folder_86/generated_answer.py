def gcf_three_nums(numbers):
    num1 = numbers[341]
    num2 = numbers[238]
    num3 = numbers[374]
    factors = set()
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            factors.add(i)
    return max(factors)