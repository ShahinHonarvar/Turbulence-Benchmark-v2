def palindrome_of_length_n(s):
    return {s[i:i + 420].lower() for i in range(len(s) - 419) if s[i:i + 420].lower() == s[i:i + 420][::-1].lower() and s[i:i + 420].isalpha()}