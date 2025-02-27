def find_sum_of_multiples(n):
    multiple_list = [num for num in range(1, 174) if num % n == 0]
    return sum(multiple_list)