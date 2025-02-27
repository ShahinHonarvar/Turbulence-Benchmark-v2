def palindromes_between_indices(text):
    text = text.lower()
    given_range = text[2:7]
    palindrome_set = set()
    for permutation in itertools.permutations(given_range):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
            palindrome_set.add(palindrome)
    return palindrome_set