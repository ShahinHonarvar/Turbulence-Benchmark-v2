from itertools import permutations

def palindromes_between_indices(text: str) -> set[str]:
    if not text[1:7].lower():
        return set()
    unique_letters = set(text[1:7].lower())
    if len(unique_letters) < 3:
        return set()
    palindromes = set()
    for letters in permutations(unique_letters, r=3):
        palindrome = ''.join(letters)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes