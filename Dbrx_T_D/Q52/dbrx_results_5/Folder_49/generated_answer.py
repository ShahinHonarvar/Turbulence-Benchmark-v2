def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 46):
        if s[i:i + 47].lower() == s[i:i + 47][::-1].lower():
            palindromes.add(s[i:i + 47])
    return palindromes