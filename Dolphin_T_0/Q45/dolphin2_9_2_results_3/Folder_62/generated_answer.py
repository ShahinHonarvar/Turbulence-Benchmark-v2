def palindromes_between_indices(s):
    string_part = s[:9]
    noise_english_letters = [char.lower() for char in string_part if char.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = list('abcdefghi')
    palindromes_set = set()
    for i in range(0, len(english_letters) + 1):
        for subset in combinations(english_letters, i):
            subset_word = ''.join(sorted(subset))
            if len(subset_word) >= 7 and is_palindrome(subset_word):
                palindromes_set.add(subset_word)
    return palindromes_set