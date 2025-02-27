from heapq import nlargest

def return_n_greatest_chars(characters):
    return sorted(nlargest(19, characters, key=ord))