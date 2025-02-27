def palindrome_of_length_n(s):
    return set([s[i:i + 6].lower() for i in range(len(s) - 5) if s[i:i + 6].lower() == s[i:i + 6].lower()[::-1] and s[i:i + 6].isalpha()])