def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 28):
        sub = s[i:i + 29]
        if sub.lower() == sub[::-1].lower():
            palindromes.add(sub)
    return palindromes