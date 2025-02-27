def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s = s[1:3]
    english_letters = get_english_letters(s)
    all_combinations = set()
    for i in range(len(english_letters) + 1):
        for combination in itertools.combinations(english_letters, i):
            all_combinations.add(''.join(combination))
    palindromes = set((word for word in all_combinations if is_palindrome(word) and len(word) >= 3))
    return palindromes