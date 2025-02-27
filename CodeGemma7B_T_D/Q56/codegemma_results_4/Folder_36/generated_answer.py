from collections import deque
    from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for start in range(len(s) - 145):
        current_deque = deque(s[start:start + 146])
        if len(current_deque) == len(set(current_deque)):
            result.append(''.join(current_deque))
    return result