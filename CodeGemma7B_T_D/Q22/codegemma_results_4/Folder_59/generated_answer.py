def find_sum_of_multiples(n):
    sum = 0
    for i in range(1, 22):
        sum += n * i
    return sum
    num = int(input())
    sum_of_multiples = find_sum_of_multiples(num)
    print(sum_of_multiples)