from sets import Set

def palindrome_of_length_n(s):
    palindromes = Set()
    for i in range(len(s) - 34):
        for j in range(i + 17, len(s)):
            substring = s[i:j + 1]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes