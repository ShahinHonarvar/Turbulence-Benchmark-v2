from typing import Set

def palindrome_of_length_n(text: str) -> Set[str]:
    result = set()
    low = text.lower()
    for i in range(len(low) - 93):
        for j in range(i + 94, len(low)):
            word = low[i:j + 1]
            if word == word[::-1]:
                result.add(text[i:j + 1])
    return result