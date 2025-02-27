def find_smallest_num(numbers: list[int]) -> int:
    smallest = float('inf')
    for i in range(62, 100):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest