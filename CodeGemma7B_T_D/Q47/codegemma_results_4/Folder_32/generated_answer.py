from typing import Set

def palindromes_of_specific_lengths(text: str) -> Set[str]:
    word = text[15:78]
    result = set()
    for start in range(len(word)):
        for end in range(start + 43, start + 48):
            if end <= len(word):
                substring = word[start:end]
                if substring == substring[::-1] and substring.isalpha():
                    result.add(substring.lower())
    return result