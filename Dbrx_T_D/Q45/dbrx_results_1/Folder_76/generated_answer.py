from collections import Set

def palindromes_between_indices(string: str) -> Set[str]:
    english_letters = set((string.lower() for string in string))
    palindromes = set()
    for i in range(1, 5):
        for j in range(i, 5):
            substring = string[i:j + 1]
            substring_set = set(substring)
            if len(substring_set) == len(substring) and len(substring) >= 4:
                palindrome = substring_set.pop()
                palindrome = ''.join(sorted(palindrome))
                palindromes.add(palindrome)
    return palindromes