def palindrome_of_length_n(txt):
    txt = txt.lower()
    palindromes = set()
    for i in range(len(txt) - 91):
        sub_txt = txt[i:i + 92]
        if sub_txt == sub_txt[::-1]:
            palindromes.add(sub_txt)
    return palindromes