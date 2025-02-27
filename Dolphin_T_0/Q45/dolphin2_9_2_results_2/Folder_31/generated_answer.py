def palindromes_between_indices(s):
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(len(s)):
        s_list = list(s)
        candidates = []
        for j in range(i, i + 9):
            if j >= 1 and j <= 8:
                candidates.extend([s_list[j], s_list[j].lower()])
        for word in candidates:
            if len(word) >= 6 and is_palindrome(word):
                palindromes.add(word)
    return palindromes