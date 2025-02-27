def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[5:10].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 6, len(letters) + 1):
            if is_palindrome(letters[i:j]):
                palindromes.add(letters[i:j])
    return {p for p in palindromes if len(p) >= 6}