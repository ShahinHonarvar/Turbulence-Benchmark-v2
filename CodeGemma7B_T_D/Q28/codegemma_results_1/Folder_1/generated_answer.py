from collections import defaultdict

def return_nth_smallest_ascii(characters):
    ascii_counts = defaultdict(int)
    for char in characters[21:60]:
        ascii_counts[ord(char)] += 1
    sorted_ascii_codes = sorted(ascii_counts.keys())
    return chr(sorted_ascii_codes[10])