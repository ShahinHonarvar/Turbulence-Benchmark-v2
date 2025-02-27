def palindrome_of_length_n(s):
    return {s[i:i + 90] for i in range(len(s) - 89) if s[i:i + 90].lower() == s[i:i + 90][::-1].lower() and s[i:i + 90].isalpha()}