from collections import Set

def palindromes_between_indices(s: str) -> Set[str]:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(2, min(8, len(s))):
        for j in range(i, min(8, len(s))):
            substring = s[i:j + 1].lower()
            if set(substring) <= english_letters and len(substring) >= 6:
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes