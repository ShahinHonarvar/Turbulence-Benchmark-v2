def find_divisors_in_range(num):
    result_list = []
    for i in range(59, 89):
        if num % i == 0:
            result_list.append(i)
    return result_list