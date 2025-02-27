import string

def palindromes_between_indices(s):
    english_letters = set(string.ascii_letters)
    palindromes = set()
    substring = ''.join((c for c in s[6:9] if c.lower() in english_letters)).lower()
    if len(substring) < 3:
        return palindromes
    for i in range(3, len(substring) + 1):
        for j in range(len(substring) - i + 1):
            candidate_palindrome = substring[j:j + i]
            if candidate_palindrome == candidate_palindrome[::-1]:
                palindromes.add(candidate_palindrome)
    return palindromes