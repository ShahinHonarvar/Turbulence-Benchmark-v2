def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 474):
        substring = s[i:i + 475]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes