def palindrome_of_length_at_least_n(txt):
    txt = txt.lower()
    palindromes = set()
    length = len(txt)
    for i in range(length):
        for j in range(i + 37, length):
            sub = txt[i:j + 1]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes