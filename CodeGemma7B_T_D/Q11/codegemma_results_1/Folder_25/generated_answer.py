def count_evens(strings):
    count = 0
    for string in strings:
        if len(string) % 2 == 0:
            count += 1
    return count