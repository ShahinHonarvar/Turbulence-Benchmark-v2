def palindromes_between_indices(s):
    s = s[1:7]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    unique_chars = set(s)
    palindromes = set()
    for char in unique_chars:
        if s.count(char) >= 2:
            temp = char * 2
            palindromes.add(temp)
    return palindromes