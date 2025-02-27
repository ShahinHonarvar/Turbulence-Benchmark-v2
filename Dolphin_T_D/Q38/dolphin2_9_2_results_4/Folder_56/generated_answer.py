def find_subset_of_length_n(elements):
    if len(elements) < 60:
        return 0
    result = 1
    for i in range(60, len(elements)):
        result *= i
    for i in range(60, 0, -1):
        result //= i
    result = result * 220
    return result