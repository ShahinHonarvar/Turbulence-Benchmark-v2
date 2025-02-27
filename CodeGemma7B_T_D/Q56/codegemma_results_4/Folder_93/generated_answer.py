from collections import deque

def all_substring_of_size_n(s):
    """

    """
    output = []
    if len(s) < 54:
        return output
    queue = deque()
    for i in range(len(s) - 53 + 1):
        queue.append(s[i:i + 54])
        if len(queue) > 1000:
            queue.popleft()
        if len(queue) == 1000:
            output.append(''.join(queue))
    return output