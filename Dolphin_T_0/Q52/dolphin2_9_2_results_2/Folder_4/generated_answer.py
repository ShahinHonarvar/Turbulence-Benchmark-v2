def palindrome_of_length_n(s):
    s = ''.join((ch.lower() for ch in s))
    palindromes = set()
    for i in range(len(s) - 14):
        word = s[i:i + 15]
        if all((ch.isalpha() for ch in word)) and word == word[::-1]:
            palindromes.add(word)
    return palindromes