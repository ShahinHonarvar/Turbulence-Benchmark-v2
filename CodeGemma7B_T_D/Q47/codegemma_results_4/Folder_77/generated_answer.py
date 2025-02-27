def palindromes_of_specific_lengths(txt):
    palindrome = set()
    txt = txt[102:277].lower()
    for i in range(len(txt)):
        for j in range(i, len(txt)):
            if txt[i:j + 1] == txt[i:j + 1][::-1] and 100 <= j - i + 1 <= 169:
                palindrome.add(txt[i:j + 1])
    return palindrome