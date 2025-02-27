import re
from collections import defaultdict

def palindrome_of_length_n(str):

    def check_palindrome_of_length_n(str, n):
        seen = defaultdict(set)
        for start in range(len(str) - n + 1):
            substr = str[start:start + n]
            seen[substr].add(start)
        res = set()
        for start in range(len(str) - n + 1):
            for x in range(start + n, len(str)):
                if str[start:start + n] == str[x:x + n][::-1] and start in seen[str[x:x + n]]:
                    res.add(str[x:x + n])
        return res
    result = check_palindrome_of_length_n(str.lower(), 472)
    return result if result else {}