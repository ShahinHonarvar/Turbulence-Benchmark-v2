from collections import deque

def palindrome_of_length_at_least_n(text):
    palindromes = set()
    queue = deque()
    letters = deque()
    for c in text.lower():
        if c.isalpha():
            letters.append(c)
            queue.append(c)
        while queue and queue[0] != letters.pop():
            queue.popleft()
        if len(queue) >= 84:
            palindromes.add(''.join(queue))
    return palindromes