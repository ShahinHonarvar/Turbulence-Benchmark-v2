from collections import deque

def insert_after_character(str):
    queue = deque()
    for char in str[::-1]:
        queue.appendleft(char)
    result = []
    while queue:
        char = queue.popleft()
        if char == 'e':
            result.append('e')
            result.append('0')
        else:
            result.append(char)
    return ''.join(result[::-1])