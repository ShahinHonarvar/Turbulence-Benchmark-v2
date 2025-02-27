def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    letters = [ch for ch in s if ch.isalpha()]
    substring = ''.join(letters[2:10]).lower()
    palindromes_set = set()
    for ch in substring:
        for combo in itertools.combinations(substring, 4 + substring.count(ch)):
            permutations = [''.join(p) for p in itertools.permutations(combo)]
            for word in permutations:
                if is_palindrome(word) and len(word) >= 4:
                    palindromes_set.add(word)
    return palindromes_set if palindromes_set else set()