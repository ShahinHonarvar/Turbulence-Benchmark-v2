def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - 97):
        sub = s[i:i + 98]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes