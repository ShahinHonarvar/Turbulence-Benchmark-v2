def palindromes_between_indices(s):
    substring = s[3:9].lower()
    substring = ''.join(filter(str.isalpha, substring))
    palindrome_set = set()
    for p in substring:
        if len(p) >= 7 and p == p[::-1]:
            palindrome_set.add(p)
    return palindrome_set