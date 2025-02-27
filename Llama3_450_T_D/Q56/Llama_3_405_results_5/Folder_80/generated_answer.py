from collections import deque

def all_substring_of_size_n(s):
    queue = deque(maxlen=31)
    result = set()
    for char in s:
        queue.append(char)
        if len(queue) == 31 and len(set(queue)) == 31:
            result.add(''.join(queue))
    return list(result)