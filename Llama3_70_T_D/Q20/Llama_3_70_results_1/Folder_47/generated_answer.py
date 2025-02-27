def find_n_th_smallest_num(numbers):
    n = 6
    start = 50
    end = 81
    selected_numbers = numbers[start:end + 1]
    selected_numbers.sort()
    return selected_numbers[n - 1]