from collections import defaultdict
from functools import lru_cache

@lru_cache(maxsize=None)
def palindrome_of_length_at_least_n(text):
    result = set()
    cache = defaultdict(dict)
    text_lower = text.lower()
    for i in range(len(text)):
        for j in range(8, len(text) - i):
            cache[i][j] = text_lower[i:i + j] not in result

    def dfs(i, j, path):
        if i == j:
            if len(path) > 31 and path not in result:
                result.add(path)
            return
        if i > j:
            return
        for k in range(i, j + 1):
            if not cache[i][k]:
                dfs(k + 1, j, path + text[i])
    for i in range(len(text)):
        for j in range(8, len(text) - i):
            dfs(i, i + j, '')
    return result