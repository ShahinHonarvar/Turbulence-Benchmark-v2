from heapq import nlargest

def return_n_smallest_chars(s: str) -> str:
    return [x[1] for x in nlargest(23, ((ord(c), c) for c in set(s)))][::-1]