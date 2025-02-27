def palindromes_between_indices(s):
    letters = [ch for ch in s[2:10] if ch.isalpha()]
    palindromes = set()

    def create_palindrome(level, word):
        if level == len(word):
            palindromes.add(word.lower())
        else:
            for ch in letters:
                create_palindrome(level + 1, word + ch)
    for length in range(7, len(letters) + 1):
        create_palindrome(0, '')
    return palindromes