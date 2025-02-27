def palindrome_of_length_n(s):
    s = s.lower()
    letters_only = ''.join(filter(str.isalpha, s))
    n = 186
    palindromes = set()
    for i in range(len(letters_only) - n + 1):
        substr = letters_only[i:i + n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes