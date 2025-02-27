from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    answer = set()
    count = defaultdict(int)
    for char in s:
        count[char] += 1
    for i in range(26):
        for j in range(i + 1):
            cases = ((i + j + 1) * count[chr(ord('a') + i)] for check in (2 * (j != i) + (j == i and count[chr(ord('a') + j)] > 1),) if all((case > 0 for case in check)))
            answer.update((''.join(sorted(word)) for word in (case + (chr(ord('a') + j),) for case in cases)))
    return answer