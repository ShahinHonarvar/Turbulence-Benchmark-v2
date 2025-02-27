def is_palindrome(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[30:96]
    for length in range(34, 56):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes