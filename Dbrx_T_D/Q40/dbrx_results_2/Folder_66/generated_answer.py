import heapq

def return_n_smallest_chars(string):
    ascii_values = [ord(char) for char in string]
    n_smallest_ascii_values = heapq.nsmallest(33, ascii_values)
    sorted_smallest_chars = [chr(ascii) for ascii in n_smallest_ascii_values]
    sorted_smallest_chars.sort(reverse=True)
    return sorted_smallest_chars