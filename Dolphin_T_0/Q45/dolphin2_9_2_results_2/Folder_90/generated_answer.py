def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1] and len(word) >= 4
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    subset = set(s[:6])
    palindromes = set()
    for i in range(4, len(english_letters) + 1):
        for subset_words in subset.combinations(i):
            for word in ''.join(subset_words).permutations():
                word = ''.join(word)
                if is_palindrome(word):
                    palindromes.add(word.lower())
    return palindromes