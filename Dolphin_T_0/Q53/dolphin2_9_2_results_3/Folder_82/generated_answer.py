def palindrome_of_length_at_least_n(s):
    s = s.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(s) - 71):
        subStr = s[i:i + 72]
        if all((char in english_letters for char in subStr)):
            if subStr == subStr[::-1]:
                palindromes.add(subStr)
    return palindromes