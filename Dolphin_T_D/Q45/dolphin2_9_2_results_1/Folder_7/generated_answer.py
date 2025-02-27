def palindromes_between_indices(s):

    def _is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    s_slice = s[1:10]
    english_letters = [c for c in s_slice if c.isalpha()]
    if len(''.join(english_letters)) < 7:
        return set()
    palindromes = set()
    for i in range(len(english_letters) - 6):
        for j in range(i + 7, len(english_letters) + 1):
            new_word = ''.join(english_letters[i:j])
            if _is_palindrome(new_word):
                palindromes.add(new_word)
    return palindromes