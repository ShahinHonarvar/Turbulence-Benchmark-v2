def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            subs = s[i:j + 1]
            if subs.lower() == subs[::-1].lower() and len(subs) >= 88:
                palindromes.add(subs)
    return palindromes