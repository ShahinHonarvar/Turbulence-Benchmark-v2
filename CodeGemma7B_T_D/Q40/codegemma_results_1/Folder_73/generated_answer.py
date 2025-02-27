import heapq

def return_n_smallest_chars(string):
    ascii_values = [(ord(char), char) for char in string]
    heapq.heapify(ascii_values)
    return sorted([char for _, char in heapq.nsmallest(80, ascii_values)])