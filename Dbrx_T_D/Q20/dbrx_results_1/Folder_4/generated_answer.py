import heapq

def find_n_th_smallest_num(numbers):
    if len(numbers) < 94 or len(numbers) - 34 < 18:
        raise ValueError('Invalid input')
    target_numbers = numbers[33:95]
    return heapq.nsmallest(18, target_numbers)[-1]