def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 77):
        substring = s[i:i + 78]
        if ''.join(reversed(substring)) == substring:
            palindromes.add(substring)
    return palindromes