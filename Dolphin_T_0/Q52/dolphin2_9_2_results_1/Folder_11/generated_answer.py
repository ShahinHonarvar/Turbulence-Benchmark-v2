def palindrome_of_length_n(s):
    letter = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 76):
        temp = s[i:i + 77]
        if all((c in letter for c in temp)):
            if temp == temp[::-1]:
                palindromes.add(temp)
    return palindromes