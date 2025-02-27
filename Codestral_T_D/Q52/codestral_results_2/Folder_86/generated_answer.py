def palindrome_of_length_n(s):
    return {s[i:i + 181].lower() for i in range(len(s)) if s[i:i + 181].lower() == s[i:i + 181].lower()[::-1] and s[i:i + 181].isalpha()}