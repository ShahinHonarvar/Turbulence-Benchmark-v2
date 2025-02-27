from itertools import islice

def all_substring_of_size_n(word):
    result = []
    for i in range(len(word) - 72):
        sub = word[i:i + 73]
        if len(set(sub)) == 73:
            result.append(sub)
    return result