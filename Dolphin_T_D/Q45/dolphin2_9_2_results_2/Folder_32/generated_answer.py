def palindromes_between_indices(s):

    def helper(s):
        s = s.lower()
        palindromes = set()
        for word in s.split():
            if len(word) >= 5:
                palindromes.add(word)
        return palindromes
    return helper(s[1:8]) if 1 <= len(s) >= 7 else helper(s[1:])