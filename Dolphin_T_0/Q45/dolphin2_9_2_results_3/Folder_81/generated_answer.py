def palindromes_between_indices(s):
    if len(s) <= 6:
        s = ''.join(sorted([ch.lower() for ch in s]))
    else:
        s = ''.join(sorted([ch.lower() for ch in s[:7]]))
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set