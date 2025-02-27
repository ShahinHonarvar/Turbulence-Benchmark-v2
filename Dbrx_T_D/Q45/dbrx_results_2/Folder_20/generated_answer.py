from functools import reduce

def palindromes_between_indices(s: str) -> set:
    chars = s[2:9].lower().replace(' ', '')
    palindromes = {word for length in range(4, len(chars) + 1) for word in {chars[i:j] for i in range(len(chars)) for j in range(i + 1, len(chars) + 1) if j - i == length} if word == word[::-1]}
    return palindromes