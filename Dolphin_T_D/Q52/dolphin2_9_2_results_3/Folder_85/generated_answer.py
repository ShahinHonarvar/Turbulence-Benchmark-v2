def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 45):
        for j in range(i + 46):
            if set(s[j:j + 46]) == set(s[j:j + 46][::-1]) and set(s[j:j + 46]).issubset(set('abcdefghijklmnopqrstuvwxyz')):
                palindromes.add(s[j:j + 46])
    return palindromes