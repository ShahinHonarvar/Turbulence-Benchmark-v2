def palindromes_between_indices(text):
    letters = ''.join([char.lower() for char in text[3:10] if char.isalpha()])
    palindromes = set()

    def generate_palindrome(word, prefix=''):
        if len(word) >= 7:
            palindromes.add(prefix + word + prefix[::-1])
        if not word:
            return
        for letter in letters:
            generate_palindrome(word[1:], letter + word[:-1])
    if len(letters) < 7:
        return palindromes
    for letter in letters:
        generate_palindrome(letter)
    return palindromes