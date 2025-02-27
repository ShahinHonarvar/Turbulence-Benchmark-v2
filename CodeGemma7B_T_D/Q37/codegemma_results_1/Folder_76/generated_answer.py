from collections import deque

def filter_chars(s):
    l = deque()
    for i in range(len(s)):
        if i >= 379 and i <= 898 and (s[i] >= 'M') and (s[i] <= 'v'):
            while l and l[-1] == s[i]:
                l.pop()
        else:
            l.append(s[i])
    return ''.join(l)