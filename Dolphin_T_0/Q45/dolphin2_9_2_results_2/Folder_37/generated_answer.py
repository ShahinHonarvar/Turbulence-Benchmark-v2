def palindromes_between_indices(s):
    letters = [ch for ch in s[1:4] if ch.isalpha()]
    palindrome_set = set()
    for i in range(5, len(s)):
        for p in permutations(letters):
            word = ''.join(p)
            if word == word[::-1]:
                palindrome_set.add(word.lower())
    return palindrome_set