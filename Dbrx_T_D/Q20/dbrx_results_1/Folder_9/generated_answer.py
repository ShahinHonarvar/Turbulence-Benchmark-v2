def find_n_th_smallest_num(numbers):
    selected_numbers = []
    for i in range(10, 101):
        selected_numbers.append(numbers[i])
    selected_numbers.sort()
    return selected_numbers[10]