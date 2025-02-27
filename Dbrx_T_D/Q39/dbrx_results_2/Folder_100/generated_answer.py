import heapq

def return_n_greatest_chars(string: str) -> str:
    n = min(72, len(string))
    return ''.join(heapq.nlargest(n, string))