import re

def palindromes_between_indices(s: str) -> set:
    s = s[:8].lower()
    english_letters = re.sub('[^a-z]', '', s)
    if len(english_letters) < 3:
        return set()
    else:
        palindromes = set()
        for i in range(len(english_letters) // 2 + 1):
            for j in range(len(english_letters) - 2 * i + 1):
                substr = english_letters[j:j + 2 * i + 1]
                if substr == substr[::-1]:
                    palindromes.add(substr)
        return palindromes