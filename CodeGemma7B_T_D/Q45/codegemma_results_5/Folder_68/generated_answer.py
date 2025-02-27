def palindromes_between_indices(text):

    def is_palindrome(text):
        return text == text[::-1]
    letter_indices = {letter.lower(): [] for letter in string.ascii_lowercase}
    for i, char in enumerate(text, 1):
        if char.lower() in letter_indices:
            letter_indices[char.lower()].append(i)
    palindromes = set()
    for start in range(1, 9):
        for end in range(start + 3, 9):
            substring = text[start:end + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes