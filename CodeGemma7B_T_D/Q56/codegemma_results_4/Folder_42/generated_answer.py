from itertools import islice

def all_substring_of_size_n(word):
    isize = 45
    result = set()
    for i in range(0, len(word) - isize + 1):
        result.add(word[i:i + isize])
    return list(result)