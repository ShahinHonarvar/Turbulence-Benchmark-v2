def find_sum_of_multiples(number):
    my_list = [number * i for i in range(1, 16)]
    total_sum = sum(my_list)
    return total_sum