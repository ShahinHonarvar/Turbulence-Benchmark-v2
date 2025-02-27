from typing import Set  

def palindromes_of_specific_lengths(s: str) -> Set[str]:
    s = s.lower()
    substring = s[16:96]
    palindromes = set()
    for i in range(len(substring) - 12):
        for j in range(i + 13, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)