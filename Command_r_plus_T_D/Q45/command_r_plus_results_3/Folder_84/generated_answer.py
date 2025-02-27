def palindromes_between_indices(s):
    s = s[4:10].lower()
    s = ''.join(filter(str.isalpha, s))
    unique_chars = set(s)
    palindromes = set()
    for char in unique_chars:
        if s.count(char) >= 2:
            i1, i2 = (s.index(char), s[::-1].index(char))
            palindrome = s[i1:i2 if i2 >= i1 else None]
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes