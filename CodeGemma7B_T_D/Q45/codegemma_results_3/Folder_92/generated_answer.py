def palindromes_between_indices(text):

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(text):
        english_letters = set()
        for char in text:
            if char.isalpha():
                english_letters.add(char.lower())
        return english_letters
    if len(text) <= 7 or text[4] == text[7]:
        return set()
    letters = get_english_letters(text[4:8])
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if is_palindrome(palindrome):
            palindromes.add(palindrome)
    return palindromes