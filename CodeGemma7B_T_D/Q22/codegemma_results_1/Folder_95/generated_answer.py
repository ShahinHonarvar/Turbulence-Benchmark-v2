def find_sum_of_multiples(num):
    multiples = []
    count = 0
    while count < 88:
        if num * count % num == 0:
            multiples.append(num * count)
            count += 1
        else:
            count += 1
    return sum(multiples)