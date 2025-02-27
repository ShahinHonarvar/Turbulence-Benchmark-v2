def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 150
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if ''.join(reversed(substring)) == substring:
            palindromes.add(substring)
    return palindromes