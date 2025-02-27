def gcf_three_nums(list):
    num_one = list[341]
    num_two = list[238]
    num_three_four = list[374]
    for i in range(1, min([num_one, num_two, num_three_four]) + 1):
        if num_one % i == 0 and num_two % i == 0 and (num_three_four % i == 0):
            gcf = i
    return gcf