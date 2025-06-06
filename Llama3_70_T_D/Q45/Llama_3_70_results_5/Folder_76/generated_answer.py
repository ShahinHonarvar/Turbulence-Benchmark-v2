def palindromes_between_indices(s):
    s = s[1:5].lower()
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i + 4, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindrome_set.add(substr)
    return palindrome_set