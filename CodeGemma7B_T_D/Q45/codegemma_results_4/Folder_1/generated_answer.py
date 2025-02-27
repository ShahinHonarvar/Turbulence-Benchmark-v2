def palindromes_between_indices(s):
    char_set = set(s[4:8].lower())
    palindrome_set = set()
    for p in product(char_set, repeat=5):
        palindrome = ''.join(p)
        if palindrome in s[4:8].lower():
            palindrome_set.add(palindrome)
    return palindrome_set