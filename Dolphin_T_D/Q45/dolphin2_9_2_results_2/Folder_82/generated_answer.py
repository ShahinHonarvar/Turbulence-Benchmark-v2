def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    s = s.lower()
    substring = s[1:7]
    letters = set(substring)
    if len(letters) < 4:
        return set()
    palindrome_set = set()
    for i in range(1, len(substring) + 1):
        for combo in itertools.combinations(letters, i):
            for perm in itertools.permutations(combo):
                possible_palindrome = ''.join(perm)
                if is_palindrome(possible_palindrome):
                    palindrome_set.add(possible_palindrome)
    return palindrome_set