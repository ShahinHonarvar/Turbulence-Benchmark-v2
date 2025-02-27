def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def create_words(word):
        words = set()
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                words.add(word[:i] + word[j] + word[i + 1:j] + word[i] + word[j + 1:])
        return words

    def find_palindromes(word):
        words = create_words(word)
        palindromes = {word for word in words if is_palindrome(word)}
        return palindromes
    if s[2:7].lower() not in 'abcdefghijklmnopqrstuvwxyz':
        return set()
    palindromes = find_palindromes(s[2:7].lower())
    return palindromes