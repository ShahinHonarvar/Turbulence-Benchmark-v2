def palindrome_of_length_n(s):
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - 5):
        sub = s[i:i + 6]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes