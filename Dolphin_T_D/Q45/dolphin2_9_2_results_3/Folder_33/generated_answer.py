def palindromes_between_indices(s):
    substring = s[7:10]
    substring_set = set(substring.lower())
    palindrome_set = set()
    for i in range(4, len(substring) + 1):
        for combo in itertools.combinations(substring_set, i):
            word = ''.join(combo)
            if word == word[::-1]:
                palindrome_set.add(word)
    return palindrome_set