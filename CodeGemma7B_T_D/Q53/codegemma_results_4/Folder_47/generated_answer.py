from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    s_lower = s.lower()
    n = 77
    output = defaultdict(list)
    for i in range(len(s_lower)):
        for j in range(i + 1, min(len(s_lower), i + 2 * n)):
            substring = s_lower[i:j]
            if substring == substring[::-1]:
                output[len(substring)].append(substring)
    return set(output[n:])