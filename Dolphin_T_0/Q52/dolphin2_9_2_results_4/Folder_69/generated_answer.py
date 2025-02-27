def palindrome_of_length_n(s):
    s = s.lower()
    set_of_palindromes = set()
    for i in range(len(s) - 471):
        sub = s[i:i + 472]
        if all((sub[j] == sub[~j] for j in range(472))):
            set_of_palindromes.add(sub)
    return set_of_palindromes