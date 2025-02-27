def palindrome_of_length_at_least_n(s):
    s = ''.join((e.lower() for e in s if e.isalpha()))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if i <= j < i + 119:
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    palindromes.add(s[i:j + 1])
    return palindromes