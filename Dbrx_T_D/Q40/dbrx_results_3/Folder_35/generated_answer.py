import heapq

def return_n_smallest_chars(string):
    ascii_values = [ord(char) for char in string]
    n_smallest_ascii_values = heapq.nsmallest(7, ascii_values)
    chars = [chr(asc) for asc in n_smallest_ascii_values]
    return sorted(chars)