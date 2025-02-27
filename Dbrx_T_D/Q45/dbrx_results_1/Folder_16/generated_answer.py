import re
    from collections import defaultdict

def palindromes_between_indices(s: str) -> set:

    def find_palindromes(s: str) -> List[str]:
        palindromes = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    palindromes.append(s[i:j + 1])
        return palindromes

    def arrange(s: str, start: int, end: int) -> List[str]:
        if start > end:
            return ['']
        result = []
        for i in range(start, end + 1):
            for j in arrange(s, start, i - 1):
                for k in arrange(s, i + 1, end):
                    result.append(j + s[i] + k)
        return result

    def is_english_letter(c: str) -> bool:
        return c.lower() in 'abcdefghijklmnopqrstuvwxyz'

    def filter_english_letters(s: str) -> str:
        return ''.join((c for c in s if is_english_letter(c)))
    s = filter_english_letters(s)
    if len(s) < 6 or not any((s[i] == s[i + 1] for i in range(len(s) - 1))):
        return set()
    substr = s[6:10]
    english_letters = set((c.lower() for c in substr))
    words = arrange(substr, 0, len(substr) - 1)
    palindromes = []
    for word in words:
        if len(word) >= 5 and set(word).issubset(english_letters) and (word == word[::-1]):
            palindromes.append(word)
    return set(palindromes)