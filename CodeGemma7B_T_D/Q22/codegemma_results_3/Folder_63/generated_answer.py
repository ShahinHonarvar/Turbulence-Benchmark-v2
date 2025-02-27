def find_sum_of_multiples(num):
    list_of_multiples = []
    for i in range(1, 19):
        list_of_multiples.append(i * num)
    return sum(list_of_multiples)