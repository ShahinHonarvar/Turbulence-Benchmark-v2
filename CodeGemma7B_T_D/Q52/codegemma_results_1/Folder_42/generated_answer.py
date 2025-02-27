def palindrome_of_length_n(s):
    palindrome = set()
    for i in range(len(s) - 279 + 1):
        for j in range(i + 1, len(s) - 278 + 1):
            if s[i:j].lower() == s[j:j + 279].lower()[::-1]:
                palindrome.add(s[i:j + 279])
    return palindrome