def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 27):
        for j in range(i, len(s) - i):
            if s[i:j + 1].lower() == s[i:j + 1][::-1].lower() and s[i:j + 1].isalpha():
                palindromes.add(s[i:j + 1])
    return {p for p in palindromes if len(p) == 28}