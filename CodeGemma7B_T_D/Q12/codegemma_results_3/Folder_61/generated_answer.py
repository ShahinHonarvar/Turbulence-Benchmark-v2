def find_smallest_num(num_list):
    return min(num_list[0:7])

def main():
    numbers = [356, 999, 6994, 356, 7781, 6, 7, 1994]
    smallest_num = find_smallest_num(numbers)
    print(smallest_num)