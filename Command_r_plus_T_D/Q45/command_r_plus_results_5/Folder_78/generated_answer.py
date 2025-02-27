def palindromes_between_indices(s):
    sub_str = s[6:9]
    english_letters = ''.join(filter(str.isalpha, sub_str)).lower()
    permutations = set(itertools.permutations(english_letters, len(english_letters)))
    palindromes = set((perm for perm in permutations if perm == perm[::-1]))
    palindromes_as_strings = set((''.join(palindrome) for palindrome in palindromes))
    return palindromes_as_strings