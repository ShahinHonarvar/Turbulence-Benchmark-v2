import re
from typing import Set

def palindrome_of_length_at_least_n(s: str) -> Set[str]:
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = set()
    for i in range(len(s) - 59):
        for j in range(i, len(s) - i):
            if j >= 59 and s[i:j + 1] == s[i:j + 1][::-1] and (s[i:j + 1] not in palindromes):
                palindromes.add(s[i:j + 1])
    return palindromes