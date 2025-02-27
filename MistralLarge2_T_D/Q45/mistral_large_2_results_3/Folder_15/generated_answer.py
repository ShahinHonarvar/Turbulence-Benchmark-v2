def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [ch for ch in s[1:3] if ch.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for start in range(len(letters) - length + 1):
            candidate = ''.join(letters[start:start + length]).lower()
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes