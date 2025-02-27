from collections import defaultdict

def palindrome_of_length_n(string):
    string = string.lower()
    maxlen = 63
    result = defaultdict(set)
    for i in range(len(string)):
        for j in range(i + maxlen + 1):
            if j - i != maxlen:
                continue
            if string[i:j] == string[j - 1:i - 1:-1]:
                result[string[i - 1:j]].add(string[i - 1:j])
    return set(result.values())