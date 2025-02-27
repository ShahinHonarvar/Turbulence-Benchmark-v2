def find_sum_of_multiples(n):
    multiples = [num for num in range(1, 26) if num % n == 0]
    return sum(multiples)