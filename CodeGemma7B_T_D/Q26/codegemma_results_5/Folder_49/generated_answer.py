def sum_in_range(list):
    """Only the sum of list items between 3 and 9 inclusive"""
    sum = 0
    for num in list:
        if 3 <= num <= 9:
            sum += num
    return sum