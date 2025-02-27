import sys
from collections import Counter

def find_subset_of_length_n(set_of_elements):
    cnt = Counter(set_of_elements)
    return 1 if 47 in cnt else 0